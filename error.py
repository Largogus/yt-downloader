errors = {
  "Connection aborted": ["E-1001", "Соединение было неожиданно разорвано."],
  "ConnectionResetError": ["E-1002", "Удалённый сервер закрыл соединение."],
  "ProxyError": ["E-1003", "Не удалось подключиться через прокси."],
  "ConnectTimeout": ["E-1004", "Превышено время ожидания подключения."],
  "ReadTimeout": ["E-1005", "Сервер отвечает слишком долго."],
  "TimeoutError": ["E-1006", "Истекло время ожидания операции."],
  "Connection refused": ["E-1007", "Сервер отклонил подключение."],
  "NameResolutionError": ["E-1008", "Не удалось определить адрес сервера."],
  "Unable to download webpage": ["E-1009", "Не удалось загрузить страницу."],

  "Video unavailable": ["E-2001", "Видео недоступно."],
  "Private video": ["E-2002", "Видео является приватным."],
  "This video is unavailable": ["E-2003", "Видео недоступно для просмотра."],
  "Video has been removed": ["E-2004", "Видео было удалено."],
  "Deleted video": ["E-2005", "Видео больше не существует."],

  "Login required": ["E-3001", "Требуется авторизация."],
  "Sign in to confirm your age": ["E-3002", "Требуется подтверждение возраста."],
  "The uploader has not made this video available in your country": ["E-3003", "Видео недоступно в вашей стране."],
  "This content isn't available": ["E-3004", "Контент недоступен."],
  "Members-only content": ["E-3005", "Контент доступен только подписчикам."],

  "Requested format is not available": ["E-4001", "Выбранный формат недоступен."],
  "No video formats found": ["E-4002", "Не найдено доступных форматов."],
  "Requested format not available": ["E-4003", "Запрошенный формат отсутствует."],

  "ffmpeg not found": ["E-5001", "Не найден FFmpeg."],
  "ffprobe not found": ["E-5002", "Не найден FFprobe."],
  "Postprocessing failed": ["E-5003", "Ошибка обработки после загрузки."],
  "Error opening input files": ["E-5004", "Не удалось открыть файлы для обработки."],

  "Permission denied": ["E-6001", "Недостаточно прав доступа."],
  "No space left on device": ["E-6002", "Недостаточно места на диске."],
  "The process cannot access the file": ["E-6003", "Файл используется другим процессом."],
  "File exists": ["E-6004", "Файл уже существует."],

  "Unsupported URL": ["E-7001", "Ссылка не поддерживается."],
  "Invalid URL": ["E-7002", "Некорректная ссылка."],
  "No video could be found in this URL": ["E-7003", "Видео по ссылке не найдено."],

  "Unable to extract": ["E-8001", "Не удалось извлечь данные."],
  "Failed to extract": ["E-8002", "Ошибка извлечения данных."],
  "Unable to extract video data": ["E-8003", "Не удалось получить информацию о видео."],
  "Unable to extract uploader id": ["E-8004", "Не удалось определить автора видео."],
  "Unable to extract initial data": ["E-8005", "Не удалось получить исходные данные."],

  "HTTP Error 403": ["E-9001", "Доступ запрещён."],
  "HTTP Error 404": ["E-9002", "Ресурс не найден."],
  "HTTP Error 429": ["E-9003", "Слишком много запросов. Попробуйте позже."],
  "HTTP Error 500": ["E-9004", "Внутренняя ошибка сервера."],
  "HTTP Error 503": ["E-9005", "Сервис временно недоступен."]
}


def get_error(err: str):
    # ERRORS = "https://raw.githubusercontent.com/Largogus/yt-downloader/refs/heads/master/errors.json"
    # errors = requests.get(ERRORS).json()

    err_lower = err.lower()

    for key, (code, desc) in errors.items():
        if key.lower() in err_lower:
            return code, desc

    return "E-9999", "Неизвестная ошибка"