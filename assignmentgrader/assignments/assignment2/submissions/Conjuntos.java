package edu.upb.estalg.analisisAlg;

import java.util.Arrays;

import edu.princeton.cs.algs4.Bag;

public class Conjuntos {

    @SuppressWarnings({ "unchecked" })
    public static <T> T[] interseccion(T[] a, T[] b) {
        T[] c = (T[]) new Object[a.length > b.length ? a.length : b.length];
        int k = 0;
        for (int i = 0; i < a.length; i++)
            for (int j = 0; j < b.length; j++)
                if (a[i].equals(b[j]))
                    c[k++] = a[i];
        return c;
    }

    @SuppressWarnings({ "unchecked" })
    public static <T> T[] diferencia(T[] a, T[] b) {
        T[] c = (T[]) new Object[a.length];
        int k = 0;
        boolean flag;
        for (int i = 0; i < a.length; i++) {
            flag = false;
            for (int j = 0; j < b.length; j++)
                if (a[i].equals(b[j]))
                    flag = true;
            if (!flag)
                c[k++] = a[i];
        }
        return c;
    }

    @SuppressWarnings({ "unchecked" })
    public static <T> T[] union(T[] a, T[] b) {
        Bag<T> set = new Bag<>();
        for (T x : a)
            set.add(x);

        for (T x : b) {
            boolean isNew = true;
            for (T y : a)
                if (y.equals(x))
                    isNew = false;
            if (isNew)
                set.add(x);
        }

        T[] r = (T[]) new Object[set.size()];
        int k = 0;
        for (T x : set)
            r[k++] = x;
        return r;
    }

    public boolean equals(Object a) {
        if (a==null) return false;
        if (! a instanceof Conjuntos) return false;
        return Arrays.equals(this, (Conjuntos)a);
    }

    public String toString() {
        s="{";
        for(T element: Conjuntos) s+=element+",";
        s += "}";
        return s;
    }

    public int hashCode() {
        return this.toString().hashCode();
    }


    public static void main(String[] args) {
        Integer[] a = { 1, 2, 3, 4, 5, 6 };
        Integer[] b = { 2, 4, 6, 8 };

        System.out.println(Arrays.toString(interseccion(a, b)));
        System.out.println(Arrays.toString(diferencia(a, b)));

        System.out.println(Arrays.toString(union(a, b)));

    }

}

