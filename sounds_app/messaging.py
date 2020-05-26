from django.core.mail import send_mail


def email_message(message_dict):
    contents = f"""
    Hi, you asked to reset your password.
    Your token is: {message_dict['token']}
    """
    send_mail(
        'Password Reset Token',
        contents,
        'robot@rtsdr.com',
        [message_dict['email']],
        fail_silently=False
    )
