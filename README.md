# django-mnemonic
## The basic code behind mnemonic-as-a-service.com

>There are only two hard things in Computer Science: cache invalidation and naming things.
>
>-- Phil Karlton

Included in this package are two django applications:

1. ```django_mnemonic``` - a django service to return words from Oren Tirosh’s [mnemonic encoding project](http://web.archive.org/web/20090918202746/http://tothink.com/mnemonic/wordlist.html).
1. ```django_mnemonic_website``` - a consumer of django_mnemonic in use at [mnemonic-as-a-service](http://mnemonic-as-a-service.com)

# Inspiration
Several weeks ago, the nice folks at [mnx.io](http://mnx.io/) wrote a fun [blog post](http://mnx.io/blog/a-proper-server-naming-scheme/) about server naming schemes.

One of the pearls of wisdom is the recommendation to use Oren Tirosh’s [mnemonic encoding project](http://web.archive.org/web/20090918202746/http://tothink.com/mnemonic/wordlist.html) as a wordlist.

GENIUS!

First I wrote a [simple flask implementation](https://github.com/alexlovelltroy/mnemonic-as-a-service) which simply returns some number of words from the wordlist and people used it. So, I created [mnemonic-as-a-service.com](http://mnemonic-as-a-service.com) to make life a little easier for the users.

# Usage

``` curl http://mnemonic-as-a-service.com/api/2 ```
