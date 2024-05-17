import engine
import village
import insects
import stars
import prologue

engine.init({"village":village.village,"insects":insects.insects,\
             "stars":stars.stars, "prologue":prologue.prologue})
engine.run("prologue")