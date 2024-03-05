# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Because it creates clusters by combining them based on closeness, agglomerative hierarchical clustering is more resistant to outliers than k-means, which is susceptible to outliers because of the mean computation."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = " k-means clustering is sensitive to initializations due to its random centroid selection, while agglomerative hierarchical clustering, once defined by a chosen linkage criterion, deterministically produces the same clustering result for a given dataset"

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "K means can take time less time, but it is not most efficent"

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "SSE of the clustering decreases."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Decrease in SSE, leads to Increase in cohesion"

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "SSB (the between sum of squares) measures the dispersion between cluster centroids. When SSB increases, it means that the centroids are moving farther away from each other, which typically indicates better separation between clusters"

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "As data points get more closely grouped within their respective clusters, increasing cohesion in k-means clustering usually results in increased dispersion between the centroids."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "The total variance of the dataset is constant, which means that the sum of SSE and BSS remains constant as the clustering changes. Therefore, SSE + SSB is indeed a constant in K-means clustering"

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "When cohesion in k-means clustering is improved, the centroids in each cluster become more distinguishable from one another because the data points are more tightly clustered within their respective clusters."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"]  = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = ""

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4* R**2"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*( a**2 + b**2 + R**2)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "10* R**2"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "When compared to the other classes, its dominating class has noticeably greater counts.Because the points within each circle are distributed uniformly, the centroids of Circle B should travel in the direction of the centroid of Circles A and C. Because the centroids would re-distribute to balance the points in each circle, each circle should have one centroid upon convergence."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Because the points on the circle are distributed uniformly, A will continue to have its centroid. With two centroids at first, Circle B may move one of its centroids to Circle C in order to equalize the point distribution. Circle B will provide one centroid to Circle C, which will start off without any. Consequently, each circle will have a single centroid following convergence."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Circle A's centroid would probably shift toward Circle B's midpoint during the k-means process since Circles A and B are substantially closer to one another. Given its greater distance from Circle B, Circle C is likely to have less of an impact on the centroids' redistribution and will likely keep its two centroids."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {"Group A","Group B"}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Group A and Group B are combined because, the distance between right most point in Group A and left most point in Group B is lesser than any point in Group C"

    # type: set
    answers["(b)"] = {"Group A","Group C"}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Considering Maximum distance between clusters, the distance between Group A and Group C have smallest distance."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {"B","C","E","F","I","J","L","M"}

    # type: set
    answers["(a) boundary"] = {"D","G"}

    # type: set
    answers["(a) noise"] = {"A","H"}

    # type: set
    answers["(b) cluster 1"] = {"B","C","E","F","G","E","D"}

    # type: set
    answers["(b) cluster 2"] = {"I","J","L","M" }

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {"B","C","D","E","F","G","I","J","L","M"}

    # type: set
    answers["(c)-a boundary"] = {"A","H"}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {"A","B","C","D","E","F","G","H","I","J","L","M"}

    # type: set
    answers["(c)-b cluster 2"] = {"A"}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 exhibits a more equitable allocation of objects among various classes in contrast to the other clusters."

    # type: string
    answers["(b)"] = "When compared to the other classes, its dominating class has noticeably greater counts."

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1"

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "A significant degree of cohesiveness within clusters is shown by the distinct and predominate blue tint in each diagonal entry.This suggests that points in the same cluster are closely clustered together, preserving a constant level of coherence throughout all clusters."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "The different hues of the off-diagonal elements in rows 1 and 3 correspond to clusters A and C, respectively.Rows 2 and 4 display comparable results for clusters B and D, respectively."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "The diagonal entries stand out from the others since they are mostly blue and clearly defined. This suggests that clusters B and C are highly cohesive."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "Different colors indicate different distances from all other clusters, while rows 1 and 4 have less defined diagonal entries.In rows two and three, two colors are displayed in the same way, suggesting that the two clusters are equally related, but that they are farther apart from each other."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Strong cohesiveness among clusters B and C is indicated by two diagonal entries that show greater clarity and intensity in blue. Within these clusters, this homogeneity points to more robust intra-cluster interactions."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "One off-diagonal entry sticks out with a distinct color in each row, while the other two have matching hues. According to this, each cluster is thought to be comparatively closer to two other clusters than it is to the third."

    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "The colors of the off-diagonal entries all vary, signifying different separations from other clusters. Clusters are separated from one another at different distances. Weaker cohesiveness within this cluster is shown by the diagonal entry's reduced definition. Cluster A will be the case."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "With a more pronounced diagonal entry, this cluster appears to have strong cohesiveness. Since B is noticeably farther from D than A and C, it is evident that two of the three off-diagonal entries have similar colors, indicating equidistant relationships. Row 2 corresponds to Cluster B."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "There appears to be strong coherence inside this cluster as the diagonal entry is more evident. As can be observed in the cases of C with B and D, when C is noticeably farther from A, two of the three off-diagonal entries have matching colors, showing equidistant relationships. Row 3 is hence Cluster C."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "Indicating differing distances from neighboring clusters, each off-diagonal entry displays a distinct hue. From other clusters, the D cluster is at different distances (it is farthest from A, and closest to C and B). Because of the less defined diagonal entry, this cluster appears to have less cohesiveness. Therefore, Cluster D will be used."

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ["hierarchical","overlapping","partial"]

    # type: list
    answers["(b)"] = ["partitional","exclusive","complete"]

    # type: list
    answers["(c)"] = ["partitional","fuzzy","complete"]

    # type: list
    answers["(d)"] = ["hierarchical","overlapping","partial"]

    # type: list
    answers["(e)"] = ["partitional","exclusive","complete"]

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "An alternative structure is a hierarchical one, in which students with comparable performance levels are put together."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "no"

    # type: string
    answers["(a) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Compared to the points between the mouth, nose, and eyes, the points in these regions are substantially closer together."

    # type: string
    answers["(b) Figure (a)"] = "no"

    # type: string
    answers["(b) Figure (b)"] = "yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The mouth, eyes, and nose would be located by K-means, but it would also include the lower density sites."

    # type: string
    answers["(c)"] = "After obtaining the new density via computing the density's reciprocal, we use DBSCAN."

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
