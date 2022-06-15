from django.shortcuts import render, HttpResponse

# Create your views here.

menu="""
    <a href="/">Inicio"</a>
    <a href="/cursos">Cursos</a>
    <a href="/contacto/">Contacto</a>
"""

def principal(request):
    contenido="<br><br><center><h1>Hola Mundo</h1><br><img src='https://i0.wp.com/unaaldia.hispasec.com/wp-content/uploads/2016/03/1b04b-django-logo.png?ssl=1' width='250'><p>Holaa... Este es mi primer sitio web con Django y Python</center>"
    return HttpResponse(menu + contenido)

def cursos(request):
    contenido="""<h2>Cursos</h2><br>
    <div class="curso" style=" background-color: #5d92c46f; text-style: none; text-decoration: none;
    color: #fff;
    font-size: 20px;
    font-family: 'Roboto', sans-serif;">
    <li>
    <br> <a href="https://platzi.com/cursos/bd/" target="-blanck">Base de Datos</a>
    <br> <a href="https://platzi.com/cursos/programacion-estructurada/" target="-blanck">Programacion</a>
    <br> <a href="https://www.djangoproject.com/" target="-blanck">Django</a>
    <br> <a href="https://flask.palletsprojects.com/en/2.1.x/" target="-blanck">Flask</a>
    <br> <a href="https://flask.palletsprojects.com/en/2.1.x/" target="-blanck">React</a>
    <br> <a href="https://platzi.com/cursos/vuejs/?gclid=CjwKCAjw14uVBhBEEiwAaufYx0uNPrqV008Rb2krYrG358OCElQow0CbQOuVXd2MaUhq5QpuJSyvlRoCVLUQAvD_BwE&gclsrc=aw.ds" target="-blanck">Vue</a>
    </li>
    </div>
    
    """
    
    return HttpResponse(menu + contenido)
def contacto(request):
    contenido="""<h2>Contacto</h2> 
    <div class="contact_form">

    <div class="formulario">      
      <h1>Formulario de contacto</h1>
        <h3>Escríbenos y en breve los pondremos en contacto contigo</h3>


          <form action="submeter-formulario.php" method="post">       

            
                <p>
                  <label for="nombre" class="colocar_nombre">Nombre
                    <span class="obligatorio">*</span>
                  </label>
                    <input type="text" name="introducir_nombre" id="nombre" required="obligatorio" placeholder="Escribe tu nombre">
                </p>
              
                <p>
                  <label for="email" class="colocar_email">Email
                    <span class="obligatorio">*</span>
                  </label>
                    <input type="email" name="introducir_email" id="email" required="obligatorio" placeholder="Escribe tu Email">
                </p>
                
                <p>
                
                <select name="color" id="color">
                    <option value="r">Base de Datos</option>
                        <option value="a">Programacion</option>
                        <option value="v">Django</option>
                        <option value="b">Flask</option>
                        <option value="c">React</option>
                        <option value="d">Vue</option>
                </select>
              
                <p>
                  <label for="asunto" class="colocar_asunto">Asunto
                    <span class="obligatorio">*</span>
                  </label>
                    <input type="text" name="introducir_asunto" id="assunto" required="obligatorio" placeholder="Escribe un asunto">
                </p>    
              
                <p>
                  <label for="mensaje" class="colocar_mensaje">Comentario
                    <span class="obligatorio">*</span>
                  </label>                     
                                    <textarea name="introducir_mensaje" class="texto_mensaje" id="mensaje" required="obligatorio" placeholder="Deja aquí tu comentario..."></textarea> 
                                </p>                    
              
                <button type="submit" name="enviar_formulario" id="enviar"><p>Enviar</p></button>

                <p class="aviso">
                  <span class="obligatorio"> * </span>los campos son obligatorios.
                </p>          
            
          </form>
    </div>  
  </div>
    """
    return HttpResponse(menu + contenido)



