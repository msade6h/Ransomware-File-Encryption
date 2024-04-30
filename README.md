**README (English)**

# Ransomware File Encryption

This Python script serves as a basic ransomware file encryption tool. It encrypts files on the user's system using a randomly generated key and the Fernet symmetric encryption algorithm from the cryptography library. Once encrypted, the original files are deleted, and the user is prompted to pay a specified amount to retrieve their data.

## How it Works

1. **Key Generation**: A random encryption key is generated using the Fernet library.

2. **Key Storage**: The generated key is saved to a file named `encryption_key.key`.

3. **File Encryption**: The script takes a target file path as input and encrypts the file using the generated key. The encrypted file is saved with an additional `.encrypted` extension appended to the original file name.

4. **Original File Deletion**: After encryption, the original file is deleted from the system.

5. **Payment Demand**: The user is informed that their files have been encrypted and they are requested to make a payment to retrieve their data.

## Usage Warning

**WARNING: This script is for educational purposes only. Do not use it for malicious intent.**

This script demonstrates the potential dangers of ransomware attacks. It should only be used in controlled environments for educational or research purposes. Any unauthorized use of this script to encrypt files without explicit consent is illegal and unethical.

---

**README (Persian)**

# رمزگذاری فایل باج‌افزار

این اسکریپت پایتون به عنوان یک ابزار پایه برای رمزگذاری فایل‌ها عمل می‌کند. این فایل‌ها را با استفاده از یک کلید تصادفی و الگوریتم رمزگذاری تقارنی Fernet از کتابخانه cryptography رمزگذاری می‌کند. پس از رمزگذاری، فایل‌های اصلی حذف می‌شوند و کاربر به پرداخت یک مبلغ مشخص برای بازیابی داده‌های خود تشویق می‌شود.

## چگونگی عملکرد

1. **تولید کلید**: یک کلید رمزگذاری تصادفی با استفاده از کتابخانه Fernet تولید می‌شود.

2. **ذخیره کلید**: کلید تولید شده در یک فایل به نام `encryption_key.key` ذخیره می‌شود.

3. **رمزگذاری فایل**: اسکریپت یک مسیر فایل هدف را به عنوان ورودی می‌گیرد و فایل را با استفاده از کلید تولید شده رمزگذاری می‌کند. فایل رمزگذاری شده با اضافه کردن پسوند `.encrypted` به نام اصلی فایل ذخیره می‌شود.

4. **حذف فایل اصلی**: پس از رمزگذاری، فایل اصلی از سیستم حذف می‌شود.

5. **درخواست پرداخت**: کاربر مطلع می‌شود که فایل‌هایش رمزگذاری شده‌اند و از او خواسته می‌شود که مبلغی مشخص را برای بازیابی داده‌های خود پرداخت کند.

## هشدار استفاده

**هشدار: این اسکریپت تنها برای اهداف آموزشی استفاده شود. لطفاً از استفاده بدون مجوز و بدون اجازه برای هر گونه موارد خلاف قوانین خودداری کنید.**

این اسکریپت نشان دهنده خطرات محتمل حملات باج‌افزار است. تنها باید در محیط‌های کنترل شده برای اهداف آموزشی یا تحقیقاتی استفاده شود. هرگونه استفاده غیرمجاز از این اسکریپت برای رمزگذاری فایل‌ها بدون رضایت صریح، غیرقانونی و غیراخلاقی است.
