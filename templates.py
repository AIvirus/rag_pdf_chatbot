css = '''
<style>
/* General styles */
body {
    background-color: #1e1e2f;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Chat container */
.chat-message {
    padding: 1.5rem;
    border-radius: 1rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: flex-start;
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    transition: transform 0.2s;
}

.chat-message:hover {
    transform: scale(1.02);
}

/* User message */
.chat-message.user {
    background: linear-gradient(135deg, #4e54c8, #8f94fb);
}

/* Bot message */
.chat-message.bot {
    background: linear-gradient(135deg, #43cea2, #185a9d);
}

/* Avatar */
.chat-message .avatar {
    width: 60px;
    height: 60px;
    margin-right: 1rem;
}

.chat-message .avatar img {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid white;
}

/* Message text */
.chat-message .message {
    flex: 1;
    color: #fff;
    font-size: 1rem;
    line-height: 1.6;
    overflow-wrap: break-word;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://img.icons8.com/?size=100&id=Ul3IIMUVd9LI&format=png&color=000000">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://img.icons8.com/?size=100&id=13042&format=png&color=000000">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
