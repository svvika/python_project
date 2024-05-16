import engine
import village
import insects

engine.init({"village": village.village, "insects": insects.insects})
engine.run("village")
