# 🔐 دليل إضافة المفاتيح في تطبيق Streamlit

## الصيغة النهائية لإضافة المفاتيح

اتبع الخطوات التالية لإضافة المفاتيح في تطبيق Streamlit Cloud أو البيئة المحلية:

---

## 1️⃣ **للبيئة المحلية (Local Development)**

### الطريقة الأولى: ملف `.streamlit/secrets.toml`

أنشئ ملف `.streamlit/secrets.toml` في جذر المشروع بالمحتوى التالي:

```toml
# ═══════════════════════════════════════════════════════════════
# Gemini API Keys (Google)
# ═══════════════════════════════════════════════════════════════
GEMINI_API_KEYS = [
    "AIzaSyBaNcbR8HKDHi8M1UjTx1d5-RqjyU4X7vQ"
]

# أو استخدم المفاتيح المنفصلة:
# GEMINI_KEY_1 = "AIzaSyBaNcbR8HKDHi8M1UjTx1d5-RqjyU4X7vQ"
# GEMINI_KEY_2 = "YOUR_SECOND_GEMINI_KEY"
# GEMINI_KEY_3 = "YOUR_THIRD_GEMINI_KEY"

# ═══════════════════════════════════════════════════════════════
# OpenRouter API Keys (متعدد النماذج)
# ═══════════════════════════════════════════════════════════════
OPENROUTER_API_KEYS = [
    "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"
]

# أو استخدم المفاتيح المنفصلة:
# OPENROUTER_KEY_1 = "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"
# OPENROUTER_KEY_2 = "YOUR_SECOND_OPENROUTER_KEY"

# ═══════════════════════════════════════════════════════════════
# Cohere API Keys
# ═══════════════════════════════════════════════════════════════
COHERE_API_KEYS = [
    "apikey-59db30b311e043ba93a2833254d7350c"
]

# أو استخدم المفاتيح المنفصلة:
# COHERE_KEY_1 = "apikey-59db30b311e043ba93a2833254d7350c"
# COHERE_KEY_2 = "YOUR_SECOND_COHERE_KEY"

# ═══════════════════════════════════════════════════════════════
# إعدادات نظام تدوير المفاتيح (اختياري)
# ═══════════════════════════════════════════════════════════════
KEY_ROTATION_ENABLED = true
KEY_ROTATION_ON_429 = true
KEY_ROTATION_STRATEGY = "round_robin"  # أو "random"

# ═══════════════════════════════════════════════════════════════
# Make.com Webhooks
# ═══════════════════════════════════════════════════════════════
WEBHOOK_UPDATE_PRICES = "https://hook.eu2.make.com/8jia6gc7s1cpkeg6catlrvwck768sbfk"
WEBHOOK_NEW_PRODUCTS = "https://hook.eu2.make.com/xvubj23dmpxu8qzilstd25cnumrwtdxm"
```

### الطريقة الثانية: متغيرات البيئة (Environment Variables)

```bash
export GEMINI_API_KEYS='["AIzaSyBaNcbR8HKDHi8M1UjTx1d5-RqjyU4X7vQ"]'
export OPENROUTER_API_KEYS='["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"]'
export COHERE_API_KEYS='["apikey-59db30b311e043ba93a2833254d7350c"]'
export KEY_ROTATION_ENABLED=true
export KEY_ROTATION_ON_429=true
```

---

## 2️⃣ **لـ Streamlit Cloud**

### الخطوات:

1. اذهب إلى [Streamlit Cloud Dashboard](https://share.streamlit.io)
2. اختر تطبيقك أو أنشئ تطبيق جديد
3. اضغط على **"Manage app"** في الزاوية اليمنى السفلى
4. اختر **"Secrets"** من القائمة الجانبية
5. انسخ والصق الكود التالي في حقل الـ Secrets:

```toml
# ═══════════════════════════════════════════════════════════════
# Gemini API Keys
# ═══════════════════════════════════════════════════════════════
GEMINI_API_KEYS = ["AIzaSyBaNcbR8HKDHi8M1UjTx1d5-RqjyU4X7vQ"]

# ═══════════════════════════════════════════════════════════════
# OpenRouter API Keys
# ═══════════════════════════════════════════════════════════════
OPENROUTER_API_KEYS = ["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"]

# ═══════════════════════════════════════════════════════════════
# Cohere API Keys
# ═══════════════════════════════════════════════════════════════
COHERE_API_KEYS = ["apikey-59db30b311e043ba93a2833254d7350c"]

# ═══════════════════════════════════════════════════════════════
# Key Rotation Settings
# ═══════════════════════════════════════════════════════════════
KEY_ROTATION_ENABLED = true
KEY_ROTATION_ON_429 = true
KEY_ROTATION_STRATEGY = "round_robin"

# ═══════════════════════════════════════════════════════════════
# Make.com Webhooks
# ═══════════════════════════════════════════════════════════════
WEBHOOK_UPDATE_PRICES = "https://hook.eu2.make.com/8jia6gc7s1cpkeg6catlrvwck768sbfk"
WEBHOOK_NEW_PRODUCTS = "https://hook.eu2.make.com/xvubj23dmpxu8qzilstd25cnumrwtdxm"
```

6. اضغط **"Save"**
7. أعد تشغيل التطبيق

---

## 3️⃣ **لـ Railway.app أو خوادم أخرى**

أضف متغيرات البيئة التالية في لوحة تحكم الخادم:

| المتغير | القيمة |
|--------|--------|
| `GEMINI_API_KEYS` | `["AIzaSyBaNcbR8HKDHi8M1UjTx1d5-RqjyU4X7vQ"]` |
| `OPENROUTER_API_KEYS` | `["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"]` |
| `COHERE_API_KEYS` | `["apikey-59db30b311e043ba93a2833254d7350c"]` |
| `KEY_ROTATION_ENABLED` | `true` |
| `KEY_ROTATION_ON_429` | `true` |
| `KEY_ROTATION_STRATEGY` | `round_robin` |

---

## 4️⃣ **صيغ بديلة لإضافة المفاتيح**

### الصيغة 1: مفتاح واحد لكل متغير

```toml
GEMINI_API_KEY = "AIzaSyBaNcbR8HKDHi8M1UjTx1d5-RqjyU4X7vQ"
OPENROUTER_API_KEY = "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"
COHERE_API_KEY = "apikey-59db30b311e043ba93a2833254d7350c"
```

### الصيغة 2: مفاتيح منفصلة مرقمة

```toml
GEMINI_KEY_1 = "AIzaSyBaNcbR8HKDHi8M1UjTx1d5-RqjyU4X7vQ"
GEMINI_KEY_2 = "YOUR_SECOND_KEY"
GEMINI_KEY_3 = "YOUR_THIRD_KEY"

OPENROUTER_KEY_1 = "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"
OPENROUTER_KEY_2 = "YOUR_SECOND_KEY"

COHERE_KEY_1 = "apikey-59db30b311e043ba93a2833254d7350c"
COHERE_KEY_2 = "YOUR_SECOND_KEY"
```

### الصيغة 3: JSON String

```toml
GEMINI_API_KEYS = '["AIzaSyBaNcbR8HKDHi8M1UjTx1d5-RqjyU4X7vQ", "KEY_2", "KEY_3"]'
OPENROUTER_API_KEYS = '["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"]'
COHERE_API_KEYS = '["apikey-59db30b311e043ba93a2833254d7350c"]'
```

---

## ✅ **التحقق من أن المفاتيح تعمل بشكل صحيح**

بعد إضافة المفاتيح، قم بتشغيل التطبيق وانتقل إلى قسم **"⚙️ الإعدادات"** ثم **"🔧 تشخيص مزودي AI"** للتحقق من:

- ✅ حالة اتصال Gemini
- ✅ حالة اتصال OpenRouter
- ✅ حالة اتصال Cohere
- ✅ عدد المفاتيح المتاحة
- ✅ إحصائيات التدوير

---

## 🔄 **كيفية عمل نظام تدوير المفاتيح الذكي**

### الميزات:

1. **التدوير التلقائي عند خطأ 429**: عند تجاوز حد الطلبات (Rate Limit)، يتم التبديل تلقائياً إلى المفتاح التالي
2. **استراتيجيات التدوير**:
   - `round_robin`: تدوير دوري منتظم (المفتاح 1 → 2 → 3 → 1)
   - `random`: اختيار عشوائي من المفاتيح المتاحة
3. **تتبع الأداء**: يتم تسجيل نجاح وفشل كل مفتاح
4. **اختيار أفضل مفتاح**: يمكن اختيار المفتاح الأفضل بناءً على الأداء التاريخي

---

## 📊 **أمثلة على الاستخدام في الكود**

### استخدام عميل Gemini المحسّن:

```python
from engines.ai_engine_enhanced import call_gemini, get_gemini_stats

# استدعاء Gemini مع تدوير ذكي تلقائي
success, response = call_gemini(
    prompt="قم بتحليل هذا المنتج: عطر ديور سوفاج",
    system_prompt="أنت خبير عطور متخصص",
    max_tokens=1000,
    temperature=0.7
)

if success:
    print(f"✅ النتيجة: {response}")
else:
    print(f"❌ الخطأ: {response}")

# عرض الإحصائيات
stats = get_gemini_stats()
print(f"معدل النجاح: {stats['success_rate']}")
print(f"عدد التدويرات: {stats['rotation_count']}")
```

---

## ⚠️ **نصائح أمان مهمة**

1. **لا تشارك المفاتيح**: لا تضع المفاتيح في الكود مباشرة أو في ملفات Git
2. **استخدم Secrets فقط**: استخدم Streamlit Secrets أو متغيرات البيئة
3. **أضف `.streamlit/secrets.toml` إلى `.gitignore`**:
   ```
   .streamlit/secrets.toml
   .env
   ```
4. **راقب الاستخدام**: تحقق من لوحة تحكم كل خدمة للتأكد من عدم الاستخدام غير المصرح

---

## 🆘 **استكشاف الأخطاء**

### خطأ: "لا توجد مفاتيح API متاحة"
- تأكد من إضافة المفاتيح في Secrets
- تحقق من اسم المتغير (يجب أن يكون `GEMINI_API_KEYS` أو `GEMINI_KEY_1`, إلخ)

### خطأ: "403 — مفتاح غير مصرح"
- تأكد من أن المفتاح صحيح ولم يتم نسخه بشكل خاطئ
- تحقق من أن المفتاح لم يتم إلغاء صلاحيته

### خطأ: "429 — تجاوز الحد"
- هذا يعني أن المفتاح الحالي قد وصل إلى حد الطلبات
- إذا كان لديك مفاتيح متعددة، سيتم التبديل تلقائياً
- إذا كان لديك مفتاح واحد فقط، انتظر قليلاً قبل إعادة المحاولة

---

## 📞 **الدعم والمساعدة**

للمزيد من المعلومات:
- [Gemini API Docs](https://ai.google.dev/gemini-api)
- [OpenRouter Docs](https://openrouter.ai/docs)
- [Cohere API Docs](https://docs.cohere.com)
- [Streamlit Secrets](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management)
