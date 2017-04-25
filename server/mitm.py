from sql import SqlHandler

sql = SqlHandler()


def Key():
    return "SuperSexySecret2FAKey"


def Post(index="*"):
    if index == "*":
        return reversed(sql.GetPosts())
    else:
        return sql.GetPosts(index)


def NewPost(title, text):
    sql.NewShortPost(title, text)
