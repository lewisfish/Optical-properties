import numpy as np
import json

is_sorted = lambda a: np.all(a[:-1] <= a[1:])


files = [f"res/water{a}.dat" for a in range(1,8)]
files.sort()

names = ["R.M. Pope et al. (1997)",
         "F.M. Sogandares et al. (1997)",
         "A. Bricaud et al. (1995)",
         "H. Buiteveld et al. (1994)",
         "R.M. Pope (1993)",
         "L. Kou et al. (1993)",
         "D.M. Wieliczka et al. (1989)"]

outd = []
for i, file in enumerate(files):
    # print(i, file)
    source = []
    x, y = np.loadtxt(file, unpack=True)
    if not is_sorted(x):
        ind = np.argsort(x)
        x = x[ind]
        y = y[ind]
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            source.append(line[1:].strip())
            if len(line) < 3:
                break
    source = "".join(source)+"\n"
    # outd.append({"wavelengths": list(x), "absoprtion": list(y), "xfmt": "nm", "yfmt": "1/cm", "source": source, "name": names[i]})
    outd = {"wavelengths": list(x), "absoprtion": list(y), "xfmt": "nm", "yfmt": "1/cm", "source": source, "name": names[i]}
    with open(f"res/{names[i]}.json", "w") as f:
        json.dump(outd, f)  