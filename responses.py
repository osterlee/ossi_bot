import random

def handle_response(user_message, message, ans):
    
  u_msg = user_message.lower()
  
  triggerlist = ['hävisin', 'hävisit', '42', 'pokemon', 'vittu', 'perkele', 'saatana', 'vitun', 'vitus', 'saatanan', 'peli', 'game', 'helvetin', 'emt', 'paska', 'helvetti']
  
  responses = ['hävisin 🤬 jumalauta', 'hävisin pelin vittu', 'vittu mä lähen tästä bändistä', 'HÄVISIN SAATANA PERKELE!', 'saatanan saatana', 'hankkikaa elämä vitun mulkut \nmul ei sellast oo ku oon pelkkä botti...', '💩 shitpost', 'prkl']
  
  if ans:
    mention = message.author.mention
    return f'Hei {mention}, hävisit juuri pelin! 👍' + '\nMiltä nyt tuntuu? Minua ainakin vituttaa.'

  else:
    if any(x in u_msg for x in triggerlist):
      return random.choice(responses)
  