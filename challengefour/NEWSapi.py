import click
import requests


prompt_test = "Enter your news source (bbc,abc,cnn,buzzfeed)."

@click.command()
@click.option('--source', prompt=prompt_test)
def cli(source):

    if source.lower() in [ 'abc','bbc', 'cnn', 'buzzfeed', 'bloomberg', 'cbc', 'focus' ]:

        if source.lower() == 'abc':
            url = 'https://newsapi.org/v2/top-headlines?sources=abc-news&apiKey=71fe483441a746bcb27a0c56db1cc460'

        elif source.lower() == 'bbc':
            url = 'https://newsapi.org/v2/top-headlines?sources=bbc-sport&apiKey=71fe483441a746bcb27a0c56db1cc460'

        elif source.lower() == 'cnn':
            url = 'https://newsapi.org/v2/top-headlines?sources=cnn&apiKey=71fe483441a746bcb27a0c56db1cc460'

        elif source.lower() == 'buzzfeed':
            url = 'https://newsapi.org/v2/top-headlines?sources=buzzfeed&apiKey=71fe483441a746bcb27a0c56db1cc460'

        elif source.lower() == 'bloomberg':
            url = 'https://newsapi.org/v2/top-headlines?sources=bloomberg&apiKey=71fe483441a746bcb27a0c56db1cc460'

        elif source.lower() == 'cbc':
            url = 'https://newsapi.org/v2/top-headlines?sources=cbc-news&apiKey=71fe483441a746bcb27a0c56db1cc460'

        elif source.lower() == 'focus':
            url = 'https://newsapi.org/v2/top-headlines?sources=focus&apiKey=71fe483441a746bcb27a0c56db1cc460'        


        news_request = requests.get(url)
        main_dict = news_request.json()
        article_dict = main_dict['articles']

        for articles in article_dict:
            click.echo(click.style('TITLE: ' + articles['title'], fg='blue'))
            click.echo(click.style('DESCRIPTION: ' +
                                articles['description'], fg='green'))
            click.echo(click.style('URL: ' +
                                articles['url'], fg='blue'))
            click.echo('\n')
            click.echo(click.wrap_text(articles['description'], 150))
            click.echo('\n')
            click.echo('-' * 150)
        
    else:
        print('source not found try searching again')
    cli()

cli()
