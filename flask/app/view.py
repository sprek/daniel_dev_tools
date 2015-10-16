import user

def get_user_list_html(db):
    users = user.get_users_from_db(db)
    users_html = '<ul>'
    for entry in users:
        users_html += '<li>' + str(entry.id_num) + '. ' + entry.name + '</li>'
    users_html += '</ul>'
    return users_html
