import engine
import village
import insects
import stars
import prologue
import carrots

engine.init({"village":village.village,"insects":insects.insects,\
             "stars":stars.stars, "prologue":prologue.prologue,
            "carrots":carrots.carrots})
engine.run("prologue")