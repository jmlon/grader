using System;
using System.Text;

public class Conjunto<T>
{
    private class Node
    {
        public T Data { get; set; }
        public Node Next { get; set; }

        public Node(T data)
        {
            Data = data;
            Next = null;
        }
    }

    private Node head;
    private int count;

    public Conjunto()
    {
        head = null;
        count = 0;
    }

    public Conjunto(T[] elementos) : this()
    {
        foreach (var elemento in elementos)
        {
            Add(elemento);
        }
    }

    public void Add(T item)
    {
        if (!Contains(item))
        {
            Node newNode = new Node(item);
            newNode.Next = head;
            head = newNode;
            count++;
        }
    }

    public bool Contains(T item)
    {
        Node current = head;
        while (current != null)
        {
            if (current.Data.Equals(item))
            {
                return true;
            }
            current = current.Next;
        }
        return false;
    }

    public Conjunto<T> Union(Conjunto<T> b)
    {
        Conjunto<T> result = new Conjunto<T>();
        Node current = head;
        while (current != null)
        {
            result.Add(current.Data);
            current = current.Next;
        }

        current = b.head;
        while (current != null)
        {
            result.Add(current.Data);
            current = current.Next;
        }

        return result;
    }

    public Conjunto<T> Interseccion(Conjunto<T> b)
    {
        Conjunto<T> result = new Conjunto<T>();
        Node current = head;
        while (current != null)
        {
            if (b.Contains(current.Data))
            {
                result.Add(current.Data);
            }
            current = current.Next;
        }
        return result;
    }

    public Conjunto<T> Diferencia(Conjunto<T> b)
    {
        Conjunto<T> result = new Conjunto<T>();
        Node current = head;
        while (current != null)
        {
            if (!b.Contains(current.Data))
            {
                result.Add(current.Data);
            }
            current = current.Next;
        }
        return result;
    }

    public Conjunto<T> DiferenciaSimetrica(Conjunto<T> b)
    {
        Conjunto<T> union = this.Union(b);
        Conjunto<T> interseccion = this.Interseccion(b);
        return union.Diferencia(interseccion);
    }

    public override bool Equals(object obj)
    {
        if (obj == null || GetType() != obj.GetType())
        {
            return false;
        }

        Conjunto<T> other = (Conjunto<T>)obj;
        if (count != other.count)
        {
            return false;
        }

        Node current = head;
        while (current != null)
        {
            if (!other.Contains(current.Data))
            {
                return false;
            }
            current = current.Next;
        }
        return true;
    }

    public override int GetHashCode()
    {
        int hash = 17;
        Node current = head;
        while (current != null)
        {
            hash = hash * 23 + current.Data.GetHashCode();
            current = current.Next;
        }
        return hash;
    }

    public override string ToString()
    {
        StringBuilder sb = new StringBuilder();
        sb.Append("{");
        Node current = head;
        while (current != null)
        {
            sb.Append(current.Data);
            if (current.Next != null)
            {
                sb.Append(",");
            }
            current = current.Next;
        }
        sb.Append("}");
        return sb.ToString();
    }

    private void Validar()
    {
        Node current = head;
        while (current != null)
        {
            Node runner = current.Next;
            while (runner != null)
            {
                if (current.Data.Equals(runner.Data))
                {
                    throw new InvalidOperationException("El conjunto contiene elementos repetidos.");
                }
                runner = runner.Next;
            }
            current = current.Next;
        }
    }

    public static void Main(string[] args)
    {
        Conjunto<int> conjuntoA = new Conjunto<int>(new int[] { 1, 2, 3, 4 });
        Conjunto<int> conjuntoB = new Conjunto<int>(new int[] { 3, 4, 5, 6 });

        Console.WriteLine("Conjunto A: " + conjuntoA);
        Console.WriteLine("Conjunto B: " + conjuntoB);

        Conjunto<int> union = conjuntoA.Union(conjuntoB);
        Console.WriteLine("Unión: " + union);

        Conjunto<int> interseccion = conjuntoA.Interseccion(conjuntoB);
        Console.WriteLine("Intersección: " + interseccion);

        Conjunto<int> diferencia = conjuntoA.Diferencia(conjuntoB);
        Console.WriteLine("Diferencia (A - B): " + diferencia);

        Conjunto<int> diferenciaSimetrica = conjuntoA.DiferenciaSimetrica(conjuntoB);
        Console.WriteLine("Diferencia Simétrica: " + diferenciaSimetrica);

        Console.WriteLine("¿Conjunto A es igual a Conjunto B? " + conjuntoA.Equals(conjuntoB));

        Conjunto<int> conjuntoC = new Conjunto<int>(new int[] { 1, 2, 3, 4 });
        Console.WriteLine("¿Conjunto A es igual a Conjunto C? " + conjuntoA.Equals(conjuntoC));
    }
}