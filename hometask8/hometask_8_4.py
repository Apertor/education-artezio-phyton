"""hometask 8.4"""
# Напишите шаблон регулярного выражения,
# который соответствовал бы следующему формату
# времени: YYYY-MM-DDThh:mm:ss±hh:mm (ISO формат).

import re

##############################################
REGEX = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}"
##############################################

MESSAGE = "Now 2020-02-17T02:02:00 by ISO format"

print(re.findall(REGEX, MESSAGE))
