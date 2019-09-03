import click
import requests

def main():
    ip = requests.get("https://api.ipify.org/?format=json").json()['ip']
    click.echo("hello world, I am at {}!".format(ip))

if __name__ == "__main__":
    main()

