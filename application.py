from flask import Flask, jsonify
application = Flask(__name__)

@application.route('/')
def index():
    return '''
    <html>
    <head><title>AWS Advanced Assignment</title></head>
    <body>
        <h1>AWS Advanced Assignment</h1>
        <p>Deployed via GitHub Actions CI/CD</p>
        <ul>
            <li>EBS + Autoscaling</li>
            <li>RDS MySQL</li>
            <li>S3 + Lifecycle</li>
            <li>Lambda + SNS + SQS</li>
            <li>DynamoDB</li>
            <li>EventBridge</li>
            <li>Secrets Manager</li>
            <li>CloudWatch</li>
        </ul>
    </body>
    </html>
    '''

@application.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    application.run(port=8000, debug=True)
