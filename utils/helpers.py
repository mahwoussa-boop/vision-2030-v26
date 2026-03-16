"""
utils/helpers.py — دوال مساعدة محسّنة لمعالجة البيانات والفلاتر
════════════════════════════════════════════════════════════════
✅ معالجة آمنة للبيانات الفارغة والمفقودة
✅ فلاتر ذكية تتعامل مع جميع الأعمدة
✅ تصدير Excel متقدم
"""
import pandas as pd
import io
import re
from typing import Dict, List, Any, Optional


def safe_float(val):
    """تحويل القيمة إلى رقم عشري بأمان"""
    try:
        if pd.isna(val) or val is None:
            return 0.0
        if isinstance(val, (int, float)):
            return float(val)
        # إزالة العملة والرموز
        s = str(val).replace('ر.س', '').replace('SR', '').replace(',', '').strip()
        return float(re.sub(r'[^\d.]', '', s))
    except:
        return 0.0


def format_price(val):
    """تنسيق السعر للعرض"""
    try:
        return f"{safe_float(val):,.2f} ر.س"
    except:
        return "0.00 ر.س"


def format_diff(val):
    """تنسيق فرق السعر"""
    try:
        val = safe_float(val)
        if val > 0:
            return f"+{val:,.2f} ر.س"
        return f"{val:,.2f} ر.س"
    except:
        return "0.00 ر.س"


def apply_filters(df, filters):
    """تطبيق الفلاتر على DataFrame"""
    if df is None or df.empty:
        return df
    
    try:
        filtered_df = df.copy()
        
        for col, val in filters.items():
            if val is None or val == "":
                continue
            
            if col not in filtered_df.columns:
                continue
            
            try:
                if isinstance(val, list):
                    filtered_df = filtered_df[filtered_df[col].isin(val)]
                elif isinstance(val, (int, float)):
                    # للأرقام، نستخدم المقارنة المباشرة
                    filtered_df = filtered_df[filtered_df[col] >= val]
                else:
                    # للنصوص، نستخدم البحث
                    filtered_df = filtered_df[
                        filtered_df[col].astype(str).str.contains(str(val), case=False, na=False)
                    ]
            except Exception as e:
                # إذا فشل الفلتر لعمود معين، نتجاهله ونستمر
                continue
        
        return filtered_df
    except Exception as e:
        return df


def get_filter_options(df: pd.DataFrame) -> Dict[str, List]:
    """
    الحصول على خيارات الفلترة من جميع الأعمدة المتاحة
    
    Args:
        df: DataFrame للحصول على الخيارات منه
    
    Returns:
        قاموس يحتوي على:
        - brands: قائمة الماركات الفريدة
        - competitors: قائمة المنافسين الفريدة
        - types: قائمة الأنواع الفريدة
    """
    options = {
        "brands": [],
        "competitors": [],
        "types": []
    }
    
    if df is None or df.empty:
        return options
    
    try:
        # البحث عن أعمدة الماركات (بأسماء مختلفة محتملة)
        brand_cols = [col for col in df.columns if 'ماركة' in col or 'brand' in col.lower() or 'العلامة' in col]
        if brand_cols:
            col = brand_cols[0]
            options["brands"] = sorted([str(x) for x in df[col].dropna().unique() if x])
        else:
            options["brands"] = ["الكل"]
        
        # البحث عن أعمدة المنافسين
        comp_cols = [col for col in df.columns if 'منافس' in col or 'competitor' in col.lower() or 'المنافس' in col]
        if comp_cols:
            col = comp_cols[0]
            options["competitors"] = sorted([str(x) for x in df[col].dropna().unique() if x])
        else:
            options["competitors"] = ["الكل"]
        
        # البحث عن أعمدة النوع
        type_cols = [col for col in df.columns if 'نوع' in col or 'type' in col.lower() or 'الفئة' in col or 'category' in col.lower()]
        if type_cols:
            col = type_cols[0]
            options["types"] = sorted([str(x) for x in df[col].dropna().unique() if x])
        else:
            options["types"] = ["الكل"]
        
        # إضافة "الكل" في بداية كل قائمة
        for key in options:
            if "الكل" not in options[key]:
                options[key] = ["الكل"] + options[key]
    
    except Exception as e:
        # في حالة الخطأ، نعيد القيم الافتراضية
        pass
    
    return options


def parse_pasted_text(text: str) -> List[Dict[str, Any]]:
    """تحليل النص الملصق لاستخراج المنتجات والأسعار"""
    products = []
    
    if not text:
        return products
    
    try:
        lines = text.strip().split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # محاولة استخراج اسم وسعر
            match = re.search(r'(\d+(?:\.\d+)?)', line)
            if match:
                try:
                    price = float(match.group(1))
                    name = line.replace(match.group(0), '').strip()
                    if name:
                        products.append({'name': name, 'price': price})
                except:
                    continue
    except Exception as e:
        pass
    
    return products


def export_to_excel(df: pd.DataFrame) -> bytes:
    """تصدير DataFrame إلى ملف Excel في الذاكرة"""
    try:
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='البيانات')
        output.seek(0)
        return output.getvalue()
    except Exception as e:
        return b""


def export_multiple_sheets(sheets_dict: Dict[str, pd.DataFrame]) -> bytes:
    """تصدير عدة جداول إلى ملف Excel واحد بصفحات متعددة"""
    try:
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            for sheet_name, df in sheets_dict.items():
                if df is not None and not df.empty:
                    # تحديد طول اسم الورقة (Excel حد أقصى 31 حرف)
                    safe_name = str(sheet_name)[:31]
                    df.to_excel(writer, index=False, sheet_name=safe_name)
        output.seek(0)
        return output.getvalue()
    except Exception as e:
        return b""


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """تنظيف DataFrame من الأخطاء والقيم الفارغة"""
    if df is None or df.empty:
        return df
    
    try:
        df = df.copy()
        
        # ملء القيم الفارغة بـ 0 للأعمدة الرقمية
        numeric_cols = df.select_dtypes(include=['number']).columns
        for col in numeric_cols:
            df[col] = df[col].fillna(0)
        
        # ملء القيم الفارغة بـ "غير محدد" للأعمدة النصية
        string_cols = df.select_dtypes(include=['object']).columns
        for col in string_cols:
            df[col] = df[col].fillna("غير محدد")
        
        return df
    except:
        return df


def get_column_by_name_variant(df: pd.DataFrame, variants: List[str]) -> Optional[str]:
    """
    البحث عن عمود في DataFrame بناءً على قائمة من الأسماء المحتملة
    
    Args:
        df: DataFrame للبحث فيه
        variants: قائمة الأسماء المحتملة
    
    Returns:
        اسم العمود إن وجد، وإلا None
    """
    if df is None:
        return None
    
    for variant in variants:
        if variant in df.columns:
            return variant
    
    return None


def safe_get_column(df: pd.DataFrame, col_name: str, default=None):
    """الحصول على عمود من DataFrame بأمان"""
    if df is None or col_name not in df.columns:
        return default
    return df[col_name]
