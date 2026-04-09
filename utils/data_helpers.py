"""
utils/data_helpers.py - دوال مساعدة لتنسيق البيانات وتوافقها مع Salla/Make
✅ دالة تنسيق المنتجات المفقودة لسلة
✅ توافق مع الإصدار v26.0
"""
import pandas as pd
import json
from typing import List, Dict, Any

def format_missing_for_salla(df: pd.DataFrame) -> List[Dict[str, Any]]:
    """
    تنسيق المنتجات المفقودة لتناسب واجهة إدخال سلة عبر Make.com
    تحويل DataFrame المفقودات إلى قائمة قواميس بالحقوق المطلوبة في سلة
    """
    if df is None or df.empty:
        return []
    
    formatted = []
    for _, row in df.iterrows():
        # استخراج القيم بأمان مع توفير بدائل
        name = str(row.get("منتج_المنافس", row.get("المنتج", ""))).strip()
        if not name:
            continue
            
        price = 0.0
        try:
            price = float(row.get("سعر_المنافس", row.get("السعر", 0)))
        except:
            price = 0.0
            
        sku = str(row.get("معرف_المنافس", row.get("SKU", ""))).strip()
        brand = str(row.get("الماركة", "")).strip()
        
        # بناء الكائن المتوافق مع CreateProduct في سلة
        item = {
            "أسم المنتج": name,
            "سعر المنتج": price,
            "رمز المنتج sku": sku,
            "الماركة": brand,
            "الوزن": 1,
            "سعر التكلفة": 0,
            "السعر المخفض": 0,
            "الوصف": f"منتج مضاف آلياً من نظام التسعير الذكي - الماركة: {brand}"
        }
        
        # إضافة صورة المنتج إذا وجدت
        if "صورة_المنتج" in row and row["صورة_المنتج"]:
            item["صورة المنتج"] = str(row["صورة_المنتج"])
            
        formatted.append(item)
        
    return formatted

def safe_results_for_json(results_list: List[Dict]) -> List[Dict]:
    """تحويل النتائج لصيغة آمنة للحفظ في JSON/SQLite"""
    safe = []
    for r in results_list:
        row = {}
        for k, v in (r.items() if isinstance(r, dict) else {}):
            if isinstance(v, list):
                try:
                    row[k] = json.dumps(v, ensure_ascii=False, default=str)
                except:
                    row[k] = str(v)
            elif pd.isna(v) if isinstance(v, float) else False:
                row[k] = 0
            else:
                row[k] = v
        safe.append(row)
    return safe

def restore_results_from_json(results_list: List[Dict]) -> List[Dict]:
    """استعادة النتائج من JSON"""
    restored = []
    for r in results_list:
        row = dict(r) if isinstance(r, dict) else {}
        for k in ["جميع_المنافسين", "جميع المنافسين"]:
            v = row.get(k)
            if isinstance(v, str):
                try:
                    row[k] = json.loads(v)
                except:
                    row[k] = []
            elif v is None:
                row[k] = []
        restored.append(row)
    return restored
