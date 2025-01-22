# Proxy
PROXY = (
    "scheme://username:password@host:port"  # оставь как есть, если прокси не нужен
)

# Parse settings
MAX_RETRIES = 3  # сколько раз повторять парсинг при ошибках
CHECK_RETWEETS = True  # проверять ли ретвиты на наличие контрактов (увеличивает количество запросов)
PARSING_INTERVAL_MINUTES = 60 # сколько минут ждать после прохода всех аккаунтов перед повторным парсингом

# X settings
BEARER_TOKEN = "your_bearer_token"

# Telegram settings
TELEGRAM_BOT_TOKEN = "your_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"
