from movies import movie_dataset, movie_labels

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def classify(unknown, dataset,labels ,k):
  distances = []
  num_good = 0
  num_bad = 0
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]
  for i in neighbors:
    title = i[1]
    if labels[title] == 0:
      num_bad+=1
    else:
      labels[title] == 0
      num_good+=1
  return 1 if num_good >= num_bad else 0

print(classify([.4, .2, .9],movie_dataset,movie_labels,5))




