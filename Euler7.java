import java.util.ArrayList;

class Euler7 {

  ArrayList<Integer> primes;

  public int nthPrime(int n) {
    primes = new ArrayList<>();
    primes.add(2);

    int current = 3;
    while (primes.size() < n) {
      if (isPrime(current)) {
        primes.add(current);
      }
      current += 2;
    }

    return primes.get(primes.size() - 1);
  }

  public boolean isPrime(int n) {
    for (int prime : primes) {
      if (n % prime == 0) {
        return false;
      }

      if (prime > Math.sqrt(n)) {
        return true;
      }
    }
    return true;
  }

  public static void main(String[] args) {
    System.out.println(new Euler7().nthPrime(10001));
  }
}
