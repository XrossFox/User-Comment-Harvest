from stackapi import StackAPI
import click


@click.command()
@click.argument('intext')
@click.argument('tagged')
@click.option('-p', default=1, help="Cantidad de Páginas")
@click.option('-s', type=click.IntRange(1,100, clamp=True), default=1,
               help="Cantidad de elementos por página, mínimo 1, máximo 100",)
def main(intext, tagged, p, s):
    """Método main del script, requiere 4 parametros al ejecutarse desde linea de comandos:
    intext: el texto a buscar en el cuerpo del texto.
    tagged: los tags con los que esta marcada la pregunta"""
    
    click.echo("Intext: {}. Tagged: {}. -p: {}. -s: {}".format(intext,tagged,p,s))
    
    response = fetch_stackapi(intext, tagged, p, s)
    maze_runner(response)
  
def fetch_stackapi(text, tags, page_size=1, max_pages=1):
    SITE = StackAPI('stackoverflow')
    SITE.page_size = page_size
    SITE.max_pages = max_pages
    return SITE.fetch('search', intext=text, tagged=tags, sort="relevance",
                          filter="!7qBwspMQR3L7c4q7tesaRX(_gP(rj*U-.H")  

def maze_runner(response):

    lista_comentarios = []
    #El response es un dict
    print("Devuelve una respuesta: {}".format(type(response)))
    print('Y contiene:')
    
    for keys in response:
        print('-'*4+" {} - que es: {}".format(keys,type(response[keys])))
        
        #items es una lista que puede tener una o más preguntas
        if keys == 'items':
            items = response[keys]
            print("-"*8+" Esta lista contiene preguntas:")
            
            #Preguntas
            for question in items:
                print("-"*8+" pregunta: {} - {}".format(type(question),repr(question)[:30]))
                
                # Cada pregunta es un diccionario
                # IMPORTANTE: La llave 'body' tiene el cuerpo de la preguta
                lista_comentarios.append(question['body'])
                # IMPORTANTE: La llave 'title' tiene el nombre de la pregunta
                
                
                for q_key in question:
                    print("-"*12+" {} que es: {}".format(q_key,type(question[q_key])))
                    
                    # Que puede tener una lista de comentarios
                    if q_key == 'comments':
                        
                        # Cada comentario es una lista
                        for comment in question[q_key]:
                            print("-"*16+" elemento: {}".format(type(comment)))
                            lista_comentarios.append(comment['body'])
                            # Que contiene un diccionario
                            for c_item in comment:
                                
                                # IMPORTANTE: La llave 'body' tiene el texto del comentario
                                print("-"*20+" {} que es: {}".format(c_item,type(c_item)))
                                
                    
                    # O una lista de respuestas
                    if q_key == 'answers':
                        
                        # Cada respuesta es un diccionario
                        # IMPORTANTE: la llave 'body' tiene el cuerpo de la respuesta
                        for comment in question[q_key]:
                            print("-"*16+" elemento: {}".format(type(comment)))
                            lista_comentarios.append(comment['body'])
                            
                            for c_item in comment:
                                print("-"*20+" {} que es: {}".format(c_item,type(comment[c_item])))
                                
                                # que puede tener una lista de comentarios
                                if c_item == 'comments':
                                    
                                    #Cada comentario es un diccionario
                                    for ind in comment[c_item]:
                                        print("-"*24+' elemento que es: {}'.format(type(ind)))
                                        lista_comentarios.append(comment['body'])
                                        
                                        # IMPORTANTE: la llave 'body' tiene el cuerpo del comentario
                                        for key_ind in ind:
                                            print("-"*28+" {} que es: {}".format(key_ind,type(ind[key_ind])))
    
    print("-"*100)
    for comentario in lista_comentarios:
        print(comentario)
        print("-"*100)
                                        
if __name__ == "__main__":
    main()