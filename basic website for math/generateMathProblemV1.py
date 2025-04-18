import json
import random

def lambda_handler(event, context):
    level = event.get('level', 1)
    
    # Generate numbers based on level
    if level == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = '+'
    elif level == 2:
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(['+', '-'])
    else:
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        operator = '*'
    
    # Calculate correct answer
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'problem': f'{num1} {operator} {num2}',
            'answer': answer
        })
    }
