package main

import (
	"github.com/gin-gonic/gin"
	"math/rand"
	"net/http"
	"strconv"
)

func init() {
	rand.Seed(52)
}

func oneword() string {
	return wordlist[rand.Intn(len(wordlist))]
}

func RandomWord(c *gin.Context) {
	wordcount := c.Params.ByName("count")
	int_wordcount, _ := strconv.Atoi(wordcount)
	// 20 is our upper limit
	if int_wordcount > 20 {
		c.Redirect(http.StatusMovedPermanently, "/mnemonic/20")
	} else {
		var words = make([]string, int_wordcount)
		for i := range words {
			words[i] = oneword()
		}
		content := gin.H{"count": int_wordcount, "words": words}
		c.JSON(200, content)
	}
}
