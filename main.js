class Singleton {
  constructor() {
    if (!Singleton.instance) {
      Singleton.instance = this;
    }
    return Singleton.instance;
  }

  // Otros métodos y propiedades de la clase pueden ir aquí
}

// Ejemplo de uso:
const instance1 = new Singleton();
const instance2 = new Singleton();

console.log(instance1 === instance2); // Debería ser true, ya que ambas variables apuntan a la misma instancia
