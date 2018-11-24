import click
import requests


prompt_test = "Enter your news source (bbc,abc,cnn,buzzfeed)."

@click.command()
@click.option('--source', prompt=prompt_test)
def cli(source):
    if source.lower() == 'abc':
        url = 'https://newsapi.org/v2/top-headlines?sources=abc-news&apiKey=71fe483441a746bcb27a0c56db1cc460'

    elif source.lower() == 'bbc':
        url = 'https://newsapi.org/v2/top-headlines?sources=bbc-sport&apiKey=71fe483441a746bcb27a0c56db1cc460'

    elif source.lower() == 'cnn':
        url = 'https://newsapi.org/v2/top-headlines?sources=cnn&apiKey=71fe483441a746bcb27a0c56db1cc460'

    elif source.lower() == 'buzzfeed':
        url = 'https://newsapi.org/v2/top-headlines?sources=buzzfeed&apiKey=71fe483441a746bcb27a0c56db1cc460'
        
    else:
        source.lower() != 'bbc', 'abc', 'cnn', 'buzzfeed'
        message = 'source not found'
        print( message )

    news_request = requests.get(url)
    main_dict = news_request.json()
    article_dict = main_dict['articles']

    for articles in article_dict:
        click.echo(click.style('TITLE: ' + articles['title'], fg='red'))
        click.echo(click.style('DESCRIPTION: ' +
                               articles['description'], fg='blue'))
        click.echo(click.style('URL: ' +
                               articles['url'], fg='red'))
        click.echo('\n')
        click.echo(click.wrap_text(articles['description'], 100))
        click.echo('\n')
        click.echo('-' * 100)
        cli()
        

cli()
