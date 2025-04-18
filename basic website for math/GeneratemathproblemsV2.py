import json
import random
import math

def generate_complex_problem(level):
    if level == 1:  # Basic arithmetic (unchanged)
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = '+'
        answer = num1 + num2
        problem = f'{num1} {operator} {num2}'
        
    elif level == 2:  # Basic arithmetic with subtraction (unchanged)
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(['+', '-'])
        answer = num1 + num2 if operator == '+' else num1 - num2
        problem = f'{num1} {operator} {num2}'
        
    elif level == 3:  # Multiplication (unchanged)
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        answer = num1 * num2
        problem = f'{num1} * {num2}'
        
    elif level == 4:  # Division with decimals
        num2 = random.randint(1, 10)
        answer = random.randint(1, 10)
        num1 = num2 * answer  # Ensures clean division
        problem = f'{num1} ÷ {num2}'
        
    elif level == 5:  # Mixed operations
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        num3 = random.randint(1, 10)
        operator1 = random.choice(['+', '-'])
        operator2 = random.choice(['*', '÷'])
        
        if operator2 == '*':
            answer = eval(f'{num1} {operator1} ({num2} * {num3})')
            problem = f'{num1} {operator1} ({num2} × {num3})'
        else:
            num2 = num2 * num3  # Ensure clean division
            answer = eval(f'{num1} {operator1} ({num2} / {num3})')
            problem = f'{num1} {operator1} ({num2} ÷ {num3})'
            
    elif level == 6:  # Powers and roots
        base = random.randint(2, 10)
        power = random.randint(2, 3)
        operation = random.choice(['power', 'root'])
        
        if operation == 'power':
            answer = base ** power
            problem = f'{base}^{power}'
        else:
            num = base ** power
            answer = base
            problem = f'∛{num}' if power == 3 else f'√{num}'
            
    else:  # Advanced - level 7
        operations = ['quadratic', 'absolute', 'factorial']
        operation = random.choice(operations)
        
        if operation == 'quadratic':
            a = random.randint(1, 5)
            b = random.randint(-10, 10)
            c = random.randint(-10, 10)
            x = random.randint(-5, 5)
            answer = a * (x ** 2) + b * x + c
            problem = f'{a}x² + {b}x + {c}, where x = {x}'
            
        elif operation == 'absolute':
            num = random.randint(-50, 50)
            answer = abs(num)
            problem = f'|{num}|'
            
        elif operation == 'factorial':
            num = random.randint(1, 7)
            answer = math.factorial(num)
            problem = f'{num}!'

    return problem, answer

def lambda_handler(event, context):
    level = event.get('level', 1)
    
    try:
        problem, answer = generate_complex_problem(level)
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'problem': problem,
                'answer': answer,
                'level': level
            })
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'error': str(e)
            })
        }
