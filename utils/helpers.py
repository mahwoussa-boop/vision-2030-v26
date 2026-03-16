import pandas as pd
import io
import re

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
    return f"{float(val):,.2f} ر.س"

def format_diff(val):
    """تنسيق فرق السعر"""
    if val > 0:
        return f"+{float(val):,.2f} ر.س"
    return f"{float(val):,.2f} ر.س"

def apply_filters(df, filters):
    """تطبيق الفلاتر على DataFrame"""
    if df is None or df.empty:
        return df
    
    filtered_df = df.copy()
    
    for col, val in filters.items():
        if val and col in filtered_df.columns:
            if isinstance(val, list):
                filtered_df = filtered_df[filtered_df[col].isin(val)]
            else:
                filtered_df = filtered_df[filtered_df[col].astype(str).str.contains(str(val), case=False, na=False)]
                
    return filtered_df

def get_filter_options(df, columns):
    """الحصول على خيارات الفلترة للأعمدة المحددة"""
    options = {}
    if df is None or df.empty:
        return {col: [] for col in columns}
        
    for col in columns:
        if col in df.columns:
            options[col] = sorted(df[col].dropna().unique().tolist())
        else:
            options[col] = []
    return options

def parse_pasted_text(text):
    """تحليل النص الملصق لاستخراج المنتجات والأسعار"""
    products = []
    lines = text.strip().split('\n')
    for line in lines:
        # محاولة بسيطة لاستخراج اسم وسعر (بافتراض وجود رقم في السطر)
        match = re.search(r'(\d+(?:\.\d+)?)', line)
        if match:
            price = float(match.group(1))
            name = line.replace(match.group(0), '').strip()
            if name:
                products.append({'name': name, 'price': price})
    return products

def export_to_excel(df):
    """تصدير DataFrame إلى ملف Excel في الذاكرة"""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    return output.getvalue()

def export_multiple_sheets(sheets_dict):
    """تصدير عدة جداول إلى ملف Excel واحد بصفحات متعددة"""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        for sheet_name, df in sheets_dict.items():
            if df is not None:
                df.to_excel(writer, index=False, sheet_name=sheet_name[:31]) # Excel sheet name limit
    return output.getvalue()
