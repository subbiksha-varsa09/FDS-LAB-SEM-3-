import matplotlib.pyplot as cricket

Overs = list(range(5, 51, 5))

Indian_Score = [30, 55, 90, 129, 165, 200, 239, 270, 310, 350]

Srilankan_Score = [25, 70, 90, 120, 140, 170, 195, 220, 255, 279]

cricket.plot(Overs, Indian_Score, color="green", label="INDIA")
cricket.plot(Overs, Srilankan_Score, color="red", label="SRILANKA")

cricket.title("INDIA Vs SRILANKA")
cricket.xlabel("Overs")
cricket.ylabel("Score")

cricket.legend(loc="center right")

cricket.show()