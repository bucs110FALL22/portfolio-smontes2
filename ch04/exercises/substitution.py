article = ("The most common New Year’s resolutions include becoming healthier and exercising more, but about 80 percent of these goals fall through by February, according to U.S. News & World Report.Swimming might be the best way for these goal-setters to stay on their targets.The enjoyment in activity is extremely important in terms of continuing to engage in those activities, says Hirofumi Tanaka, a professor in the University of Texas’s Department of Kinesiology and Health Education.Tanaka points to a study of minimally to moderately obese young women done by Grant Gwinup and published in the American Journal of Sports Medicine in 1987. Participants reported that they enjoyed swimming much more than running and cycling. Swimming is also the third-most popular exercise, according to the most recent data available from the U.S. Census Bureau, meaning you’ll have someone to work out with.")

test = {
  "Swimming":"Running",
  "February":"April",
  "Professor":"Teacher",
  "Have":"Had",
  "according":"HAHA"
}

for key, value in test.items():
  article = article.replace(key, value)

print(article)

