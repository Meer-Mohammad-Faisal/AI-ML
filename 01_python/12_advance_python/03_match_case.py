def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internal sever Error"
        case _:
            return "Unknown status"

print(http_status(500))