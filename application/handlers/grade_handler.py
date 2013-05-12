# -*- encoding: utf-8 -*-

from flask import g, redirect, request, jsonify


err_message = {
    'required_grade': '-1',
    'description': 'Média não reconhecida',
    'badge_class': 'badge badge-important',
    'alert_class': 'alert alert-error'
}

messages_for_grades = [
    {
        'min': 3,
        'max': 3.499,
        'description': 'Mermão, num sei nem se vale a pena estudar pra essa prova...',
        'badge_class': 'badge badge-important',
        'alert_class': 'alert alert-error',
    },
    {
        'min': 3.499,
        'max': 3.999,
        'description': 'Eu não queria estar na sua pele.',
        'badge_class': 'badge badge-important',
        'alert_class': 'alert alert-error',
    },
    {
        'min': 3.999,
        'max': 4.7499,
        'description': 'Sua situação é tensa e dramática, mas tenha fé. E café.',
        'badge_class': 'badge badge-warning',
        'alert_class': 'alert alert-block',
    },
    {
        'min': 4.7499,
        'max': 5.2499,
        'description': 'Só repete o que fez até agora.',
        'badge_class': 'badge badge-warning',
        'alert_class': 'alert alert-block',
    },
    ,
    {
        'min': 5.2499,
        'max': 5.99,
        'description': 'Você poderia estar pior, mas pra quem tá na final, tá até bem.',
        'badge_class': 'badge badge-warning',
        'alert_class': 'alert alert-block',
    },
    {
        'min': 5.99,
        'max': 6.499,
        'description': 'Aí tá fácil, né?',
        'badge_class': 'badge badge-success',
        'alert_class': 'alert alert-success',
    },
    {
        'min': 6.499,
        'max': 7,
        'description': 'Tá de sacanagem! Você conseguiu ir pra final?',
        'badge_class': 'badge badge-success',
        'alert_class': 'alert alert-success',
    }
]


def get_required_grade_for_average(avg):
    base_value = round(12.5 - (avg*1.5), 2)
    return base_value if base_value > 3 else 3


def get_details_for_required_grade(required_grade):
    for message in messages_for_grades:
        if message['min'] <= required_grade <= message['max']:
            return message['description'], message['badge_class'], message['alert_class']


def get_message_for_average_grade(avg):

    message = err_message.copy()

    if avg is None or not is_number(avg):
       return err_message
    
    avg = float(avg)

    if avg > 10 or avg < 0:
        return err_message

    required_grade = get_required_grade_for_average(avg) 
    if avg < 3:
        message['description'] = 'É, mermão... mais sorte da próxima vez!'
        message['required_grade'] = 'Mais de 9 mil...'
    elif avg >= 7:
        message['description'] = 'Você não precisa fazer final, seu zé.'
        message['required_grade'] = 'porrada'
    else:
        description, badge_class, alert_class = get_details_for_required_grade(avg)
        message['description'] = description
        message['badge_class'] = badge_class
        message['alert_class'] = alert_class
        message['required_grade'] = get_required_grade_for_average(avg)

    return message


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def average_grade():
    
    avg = request.args.get('avg', None)

    if avg:
        avg = avg.replace(',', '.')

    return jsonify(get_message_for_average_grade(avg))
