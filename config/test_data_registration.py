# Данные для тестирования формы регистрации
reg_name = 'Имя'
reg_surname = 'Фамилия'
reg_email = 'natanieo@gmail.com'
reg_phone = '+79149648255'
reg_pass = 'Ntcns24@'

incorrect_reg_names = ["", "А", "У"*31, "a"*10, "И"*256, "的一了是我不在人们有", 1234567890, "о"*1001, "/'}{[]<>№;%:?*()"]
incorrect_reg_names_ids = [
    "Empty string",
    "One char",
    "31 cyrillic chars",
    "10 latin chars",
    "Cyrillic string with 256 chars",
    "10 chinese chars",
    "Digits",
    "Cyrillic string >1000 chars",
    "Spec.symbols string"
]

incorrect_email_phone = ["", "@test.ru", "f"*256, 'y'*1001, "/'}{[]<>№;%:?*()",
                         "тест@тест.рф", "的一了是我不在人们有", "+7999999999",
                         "+799999999999", "+49111111111"]
incorrect_email_phone_ids = [
    "Empty string",
    "@test.ru (without the beginning)",
    "Latin string with 256 chars",
    "Latin string >1000 chars",
    "Spec.symbols string",
    "Cyrillic email (тест@тест.рф)",
    "Chinese chars",
    "Ph.number with +7 but only 9 digits",
    "Ph.number with +7 but 11 digits",
    "Ph.number with +49 country code and 9 digits"
]

incorrect_reg_pass_with_alerts = [
    ("", "Длина пароля должна быть не менее 8 символов"),
    ("a"*7, "Длина пароля должна быть не менее 8 символов"),
    (12345678, "Пароль должен содержать хотя бы одну заглавную букву"),
    ("б"*8, "Пароль должен содержать только латинские буквы"),
    ("A12345678", "Пароль должен содержать хотя бы одну строчную букву"),
    ("abcdabcd", "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"),
    ("的一了是我不在人们有", "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"),
    ("}{[]'<>/№;%:?*()", "Пароль должен содержать хотя бы одну заглавную букву"),
    ("f"*256, "Длина пароля должна быть не более 20 символов"),
    ('y'*1001, "Длина пароля должна быть не более 20 символов")
]
incorrect_reg_pass_ids = [
    "Empty string",
    "7 Latin chars",
    "8 digits",
    "8 Cyrillic chars",
    "Upper latin char and 8 digits",
    "8 lower latin chars",
    "Chinese chars",
    "Spec.symbols string",
    "Latin string with 256 chars",
    "Latin string >1000 chars"
]