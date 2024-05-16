import engine
import village
import insects
import stars
engine.init({"village":village.village,"insects":insects.insects,\
             "stars":stars.stars})
engine.run("village")
