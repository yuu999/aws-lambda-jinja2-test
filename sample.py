# coding: utf-8
import json
import logging
import urllib.parse

from jinja2 import Environment, FileSystemLoader

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    logging.info(f'event: {event}')

    # header Content-Type must be application/x-www-form-urlencoded
    source_ip = event['requestContext']['identity']['sourceIp']
    agent = event['requestContext']['identity']['userAgent']
    method = event['httpMethod']

    # --- Genarate HTML ------------------------------------------------------
    env = Environment(loader=FileSystemLoader('./template', encoding='utf8'))
    tpl = env.get_template('template.html')

    data = {
        "method": method,
        "source_ip": source_ip,
        "agent": agent,
        "event": json.dumps(event, indent=4)
    }

    html = tpl.render(data)
    logging.info(f'sourceIP: {source_ip}')

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': html
    }
