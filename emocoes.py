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


def aplicastemmer(texto):
        stemmer = nltk.stem.RSLPStemmer()
        frasesstemmer = []
        for (palavra, emocao) in texto:
                comstemmer = [str (stemmer.stem(p)) for p in palavra.split() if p not in stopwordsnltk]
                frasesstemmer.append((comstemmer, emocao))
        return frasesstemmer

stemmer = aplicastemmer(base)

def pegarpalavras(texto):
        todaspalavras = []
        for (palavra, emocao) in texto:
               todaspalavras.extend(palavra)
        return todaspalavras

palavras = pegarpalavras(stemmer)

def pegafrequencia(text):
        text = nltk.FreqDist(palavras)
        return text

frequencia = pegafrequencia(palavras)

def palavrasunicas(frequencia):
        freq = frequencia.keys()
        return freq

palavrasunicas = palavrasunicas(frequencia)

def extrairpalavras(documento):
        doc = set (documento)
        caracteristicas = {}
        for palavras in palavrasunicas:
                caracteristicas['%s' % palavras] = palavras in doc
        return caracteristicas

baseprocessada = nltk.classify.apply_features(extrairpalavras, stemmer)


