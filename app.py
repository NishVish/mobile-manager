from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mobile Manager</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0b0f19;
            --card-bg: rgba(255, 255, 255, 0.03);
            --border-color: rgba(255, 255, 255, 0.08);
            --accent-primary: #3b82f6;
            --accent-secondary: #8b5cf6;
            --text-primary: #f3f4f6;
            --text-secondary: #9ca3af;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            position: relative;
        }

        /* Ambient background glow */
        body::before {
            content: '';
            position: absolute;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(59, 130, 246, 0.15) 0%, rgba(139, 92, 246, 0.05) 50%, transparent 100%);
            top: -200px;
            left: -200px;
            z-index: 0;
            pointer-events: none;
        }

        body::after {
            content: '';
            position: absolute;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(139, 92, 246, 0.15) 0%, rgba(59, 130, 246, 0.05) 50%, transparent 100%);
            bottom: -200px;
            right: -200px;
            z-index: 0;
            pointer-events: none;
        }

        .container {
            z-index: 1;
            text-align: center;
            padding: 3rem;
            border-radius: 24px;
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3);
            max-width: 500px;
            width: 90%;
            animation: fadeIn 1s ease-out;
        }

        .logo-container {
            display: inline-flex;
            justify-content: center;
            align-items: center;
            width: 80px;
            height: 80px;
            border-radius: 20px;
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            margin-bottom: 2rem;
            box-shadow: 0 8px 24px rgba(59, 130, 246, 0.3);
            animation: float 4s ease-in-out infinite;
        }

        .logo-icon {
            font-size: 2.5rem;
            color: #fff;
        }

        h1 {
            font-size: 2.2rem;
            font-weight: 800;
            background: linear-gradient(135deg, #ffffff 30%, #a5b4fc 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
            letter-spacing: -0.5px;
        }

        p {
            font-size: 1.1rem;
            color: var(--text-secondary);
            line-height: 1.6;
            margin-bottom: 2rem;
        }

        .badge {
            display: inline-block;
            padding: 0.5rem 1rem;
            border-radius: 9999px;
            background: rgba(59, 130, 246, 0.1);
            color: var(--accent-primary);
            font-size: 0.85rem;
            font-weight: 600;
            border: 1px solid rgba(59, 130, 246, 0.2);
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .badge:hover {
            background: rgba(59, 130, 246, 0.2);
            transform: translateY(-2px);
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes float {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-8px);
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="logo-container">
            <span class="logo-icon">📱</span>
        </div>
        <h1>Hello, this is Mobile Manager</h1>
        <p>Your premium dashboard for managing and orchestrating mobile devices, applications, and system deployments seamlessly.</p>
        <div class="badge">v1.0.0 Stable</div>
    </div>
</body>
</html>
"""

@app.route('/')
def hello():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
