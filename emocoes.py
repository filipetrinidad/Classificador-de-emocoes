import nltk

base = [('Eu estou muito feliz', 'alegria'),
        ('Nós estamos alegres', 'alegria'),
        ('Me sinto amavel', 'alegria'),
        ('Me considero afortunado', 'alegria'),
        ('Sou prospero', 'alegria'),
        ('Me diverti muito', 'alegria'),
        ('Estou alegre por voce', 'alegria'),
        ('Acordei muito bem', 'alegria'),
        ('ele está atimo', 'alegria'),
        ('Hoje é um otimo dia para ser feliz', 'alegria'),
        ('Estou apavorado', 'medo'),
        ('Sinto medo disso', 'medo'),
        ('Isso me causa aflição', 'medo'),
        ('Me assustei', 'medo'),
        ('Que aflicao', 'medo'),
        ('Cuidado com os males', 'medo'),
        ('Estou tremendo de tanto medo', 'medo'),
        ('Você está assustado', 'medo'),
        ('que pavor', 'medo'),
        ('voce e um covarde', 'medo')]

stopwordsnltk = nltk.corpus.stopwords.words('portuguese')

def removestopwords(texto):
        frases = []
        for (palavras, emocao) in texto:
                semstopwords = [p for p in palavras.split() if p not in stopwordsnltk]
                frases.append((semstopwords, emocao))
        return frases

print(removestopwords(base))