from src.polynomial.xgcd import xgcd, gcd

if __name__ == "__main__":
    a = [0,1]
    b = [0]
    m = 2
    print("result", xgcd(a, b, m))