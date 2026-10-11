import pandas as pd

structured_data = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

print("Structured Data:")
print(structured_data)

unstructured_data = """This is an example of unstructured data.
It can be a piece of text, an image, or a video file."""

print("\nUnstructured Data:")
print(unstructured_data)


semi_structured_data = {
    'ID': 1,
    'Name': 'Alice',
    'Attributes': {
        'Height': 165,
        'Weight': 68
    }
}

print("\nSemi-structured Data:")
print(semi_structured_data)