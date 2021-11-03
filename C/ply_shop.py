from ply import lex, yacc

tokens = (
    'NUMBER',
    'OPERATE',
    'SIZE',
    'KIND',
    'COLOR',
    'MATERIAL',
    'QUESTION_HOW',
    'QUESTION_MANY'
)


# A regular expression rules with some action code
def t_NUMBER(t):
    r"""\d+"""
    t.value = int(t.value)
    return t


def t_COLOR(t):
    r"""black | white | red | green | blue"""
    if t.value == 'black':
        t.value = 1
    elif t.value == 'white':
        t.value = 2
    elif t.value == 'red':
        t.value = 3
    elif t.value == 'green':
        t.value = 4
    elif t.value == 'blue':
        t.value = 5
    return t


def t_MATERIAL(t):
    r"""metal | plastic"""
    if t.value == 'metal':
        t.value = 1
    elif t.value == 'plastic':
        t.value = 2
    return t


def t_SIZE(t):
    r"""tiny | small | big | large"""
    if t.value == 'tiny':
        t.value = 1
    elif t.value == 'small':
        t.value = 2
    elif t.value == 'big':
        t.value = 3
    elif t.value == 'large':
        t.value = 4
    return t


def t_KIND(t):
    r"""box(es)? | ring(s)?"""
    if t.value[0] == 'b':
        t.value = 1
    else:
        t.value = 2
    return t


def t_OPERATE(t):
    r"""Buy | Sell"""
    return t


def t_QUESTION_HOW(t):
    r"""How"""
    return t


def t_QUESTION_MANY(t):
    r"""many"""
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Initialize table of articles
tab = []
for i in range(3000):
    tab.append(0)

# Build the lexer
lexer = lex.lex()


def p_command_operate(p):
    """command : OPERATE NUMBER article"""
    index = p[3]
    # Buy article
    if p[1] == 'Buy':
        tab[index] += p[2]
        print('OK. I am buying ', str(p[2]), 'new articles indexed as ', str(index), '.')
        print('Number of articles in shop: ', str(tab[index]))
    # Sell article
    elif p[1] == 'Sell':
        if p[2] > tab[index]:
            print('I do not have as many articles as you want.')
        else:
            tab[index] -= p[2]
            print('OK. I am selling ', str(p[2]), 'new articles indexed as ', str(index), '.')
            print('Number of articles in shop: ', str(tab[index]))


def p_command_question(p):
    """command : QUESTION_HOW QUESTION_MANY article"""
    print('Number of articles in shop indexed as', str(p[3]), ':', str(tab[p[3]]))


def p_article_attribute(p):
    """article : attribute article"""
    p[0] = p[1] + p[2]


def p_attribute_color(p):
    """attribute : COLOR"""
    p[0] = p[1]


def p_attribute_material(p):
    """attribute : MATERIAL"""
    p[0] = 10 * p[1]


def p_attribute_size(p):
    """attribute : SIZE"""
    p[0] = 100 * p[1]


def p_article_kind(p):
    """article : KIND"""
    p[0] = 1000 * p[1]


def p_error(t):
    print("Syntax error at '%s'" % t.value)


# Build the parser
parser = yacc.yacc()


def nlp_ply():
    # Main loop
    while True:
        s = input('\nWhat can I do for you?\n')
        if s == 'Bye':
            break
        parser.parse(s)


if __name__ == "__main__":
    nlp_ply()
