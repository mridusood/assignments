import re
emails = '''zuck26@facebook.com
page33@google.com
jeff42@amazon.com'''

pattern = '(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})'
p=re.findall(pattern, emails, flags=re.IGNORECASE)

print(p)

#ques2
text='''
Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter 
better.'''
m = re.findall('[B,b]\w+', text)
print (m)

#ques3
sentence = "A, very very; irregular_sentence"
x=re.compile("[,;_]")
y=x.sub(" ",sentence)
print(y)

#optional_ques
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today 
http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
def abc(tweet):
    tweet = re.sub('http\S+\s*', '', tweet)
    tweet = re.sub('RT|cc', '', tweet)
    tweet = re.sub('#\S+', '', tweet)
    tweet = re.sub('@\S+', '', tweet)
    tweet = re.sub('[%s]' % re.escape(""":!"""), '', tweet)
    tweet = re.sub('\s+', ' ', tweet)
    return tweet

print(abc(tweet))