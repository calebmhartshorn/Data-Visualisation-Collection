load(file='< PATH >/BoardGames.rda')

library(tidyverse)
library(plotly)

p <- BoardGames |> 
  filter(details.yearpublished >= 1950) |>
  filter(stats.subtype.boardgame.bayesaverage >= 5) |>
  ggplot(aes(x = details.yearpublished, y = stats.subtype.boardgame.bayesaverage, text = details.name)) +
  geom_point(color = "#ffffff", alpha = (1/10)) + 
  theme(
    plot.background = element_rect(fill = "#000000"),
    panel.background = element_rect(fill = "#000000"),
    panel.grid = element_blank(),
    text = element_text(colour = "#999999"),
    axis.text = element_text(colour = "#999999")
    
  ) + 
  labs(
    title = "Board Game Geek Rating by Year Published",
    x = "Year Published",
    y = "Average Rating (0-10)"
  )
ggplotly(p)
