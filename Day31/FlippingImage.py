def flipAndInvertImage(image):
    for r in image:
        l, h = 0, len(r) - 1
        while l <= h:
            r[l], r[h] = r[h] ^ 1, r[l] ^ 1
            l += 1
            h -= 1
    return image

if __name__ == "__main__":
    import ast
    image = ast.literal_eval(input("Enter 2D image array: "))
    result = flipAndInvertImage(image)
    print(result)
