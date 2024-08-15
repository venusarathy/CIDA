from concurrent.futures import ProcessPoolExecutor, as_completed
from itertools import permutations

# Is really applies permutation with given decoders
def apply_permutation(input_str, permutation):
    try:
        result = input_str
        for func in permutation:
            result = func(result)
        funcs = " -> ".join([func.__name__ for func in permutation])
        return (funcs, result)
    except Exception as e:
        funcs = " -> ".join([func.__name__ for func in permutation])
        return (funcs, f"Error: {e}")

def process_permutations(input_str, function_permutations):
    results = []
    with ProcessPoolExecutor() as executor:
        future_to_permutation = {executor.submit(apply_permutation, input_str, permutation): permutation for permutation in function_permutations}
        
        try:
            for future in as_completed(future_to_permutation):
                result = future.result()
                results.append(result)
                funcs, output = result
                print(f"Permutation: {funcs}")
                print(f"Result: {output}\n")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            executor.shutdown(wait=True)  # Ensure all processes are cleaned up

    return results

def generate_permutations(conversion_functions, depth):
    return permutations(conversion_functions, depth)

