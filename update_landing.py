import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Brand Name
html = html.replace("ConvivePro", "Convive+")

# 2. Hero Section
html = html.replace(
    'Digitaliza la gestión de <br class="hidden lg:block" />\n                    <span\n                        class="text-transparent bg-clip-text bg-gradient-to-r from-cp-brand to-cp-accent inline-block overflow-visible py-2">\n                        convivencia escolar\n                    </span>',
    'Digitaliza la gestión de <br class="hidden lg:block" />\n                    <span\n                        class="text-transparent bg-clip-text bg-gradient-to-r from-cp-brand to-cp-accent inline-block overflow-visible py-2">\n                        convivencia escolar\n                    </span><br/>en tu colegio'
)

html = html.replace(
    'Convive+ permite registrar incidentes, gestionar evidencias y analizar casos de convivencia\n                    escolar de forma clara, ordenada y profesional.',
    'Construye un clima positivo. Convive+ te permite registrar incidentes, almacenar evidencias y hacer seguimiento de casos para tomar decisiones disciplinarias informadas, reemplazando el uso de papel.'
)

html = html.replace(
    '<button\n                        class="bg-cp-surface dark:bg-[theme(colors.cp.dark.surface.1)] border-2 border-cp-border dark:border-[theme(colors.cp.dark.border.DEFAULT)] px-8 py-4 rounded-xl text-lg font-bold text-cp-text dark:text-[theme(colors.cp.dark.text.DEFAULT)] hover:bg-cp-surface-2 dark:hover:bg-[theme(colors.cp.dark.surface.2)] hover:-translate-y-1 hover:shadow-lg transition-all duration-300 active:scale-95">\n                        Ver cómo funciona\n                    </button>',
    '<a href="#proceso" \n                        class="inline-flex items-center justify-center bg-cp-surface dark:bg-[theme(colors.cp.dark.surface.1)] border-2 border-cp-border dark:border-[theme(colors.cp.dark.border.DEFAULT)] px-8 py-4 rounded-xl text-lg font-bold text-cp-text dark:text-[theme(colors.cp.dark.text.DEFAULT)] hover:bg-cp-surface-2 dark:hover:bg-[theme(colors.cp.dark.surface.2)] hover:-translate-y-1 hover:shadow-lg transition-all duration-300 active:scale-95">\n                        Ver cómo funciona\n                    </a>'
)

# 3. Problem Section
html = html.replace(
    'La convivencia escolar aún se gestiona con papel',
    'El costo del desorden y el uso de papel'
)
html = html.replace(
    'La falta de\n                    digitalización genera brechas críticas en la administración de la convivencia escolar.',
    'Gestionar la convivencia escolar con métodos tradicionales genera desgaste innecesario y dificulta la toma de decisiones.'
)

html = html.replace(
    '<h3 class="text-xl font-bold mb-3">Información dispersa</h3>\n                    <p\n                        class="text-cp-text-secondary dark:text-[theme(colors.cp.dark.text.secondary)] text-sm leading-relaxed">\n                        Documentos en carpetas físicas y archivos aislados difíciles de localizar en momentos críticos.\n                    </p>',
    '<h3 class="text-xl font-bold mb-3">Uso excesivo de papel</h3>\n                    <p\n                        class="text-cp-text-secondary dark:text-[theme(colors.cp.dark.text.secondary)] text-sm leading-relaxed">\n                        Libros de clases y formularios físicos que generan desorden, pérdida de información y daño de documentos importantes.\n                    </p>'
)

html = html.replace(
    '<h3 class="text-xl font-bold mb-3">Dificultad de historial</h3>\n                    <p\n                        class="text-cp-text-secondary dark:text-[theme(colors.cp.dark.text.secondary)] text-sm leading-relaxed">\n                        Es casi imposible reconstruir la línea de tiempo disciplinaria de un alumno sin horas de\n                        búsqueda.</p>',
    '<h3 class="text-xl font-bold mb-3">Información dispersa</h3>\n                    <p\n                        class="text-cp-text-secondary dark:text-[theme(colors.cp.dark.text.secondary)] text-sm leading-relaxed">\n                        Anotaciones aisladas y fragmentadas que impiden tener un panorama claro y centralizado del comportamiento del alumno.</p>'
)

html = html.replace(
    '<h3 class="text-xl font-bold mb-3">Falta de trazabilidad</h3>\n                    <p\n                        class="text-cp-text-secondary dark:text-[theme(colors.cp.dark.text.secondary)] text-sm leading-relaxed">\n                        Incertidumbre total sobre qué acciones se tomaron, cuándo y quién fue el responsable del caso.\n                    </p>',
    '<h3 class="text-xl font-bold mb-3">Ausencia de seguimiento</h3>\n                    <p\n                        class="text-cp-text-secondary dark:text-[theme(colors.cp.dark.text.secondary)] text-sm leading-relaxed">\n                        No hay forma clara de dar seguimiento a los casos abiertos, compromisos adquiridos ni medidas disciplinarias aplicadas.\n                    </p>'
)

html = html.replace(
    '<h3 class="text-xl font-bold mb-3">Ausencia de datos</h3>\n                    <p\n                        class="text-cp-text-secondary dark:text-[theme(colors.cp.dark.text.secondary)] text-sm leading-relaxed">\n                        Imposibilidad de detectar patrones o tendencias de convivencia para la toma de decisiones\n                        preventiva.</p>',
    '<h3 class="text-xl font-bold mb-3">Falta de estadísticas</h3>\n                    <p\n                        class="text-cp-text-secondary dark:text-[theme(colors.cp.dark.text.secondary)] text-sm leading-relaxed">\n                        Sin reportes ni dashboards en tiempo real es imposible entender el clima escolar y accionar tempranamente.</p>'
)

# 4. Solucion & Cards
html = html.replace(
    'Una plataforma diseñada para\n                        convivencia escolar',
    'La solución centralizada para un colegio organizado'
)
html = html.replace(
    'Centralice la información y tome decisiones organizadas con un flujo de trabajo profesional\n                        diseñado específicamente para directivos y equipos de convivencia.',
    'Convive+ centraliza tus registros, otorga orden administrativo, asegura el control total de los expedientes y garantiza la trazabilidad de cada acción disciplinaria tomada por el equipo.'
)

html = html.replace(
    '<h4 class="font-bold text-lg mb-1">Cumplimiento Normativo</h4>\n                                <p\n                                    class="text-cp-text-secondary dark:text-[theme(colors.cp.dark.text.secondary)] text-sm">\n                                    Cumplimiento total con normativas educacionales locales exigidas.</p>',
    '<h4 class="font-bold text-lg mb-1">Total Trazabilidad</h4>\n                                <p\n                                    class="text-cp-text-secondary dark:text-[theme(colors.cp.dark.text.secondary)] text-sm">\n                                    Seguimiento claro y documentado de cada fase de los casos escolares.</p>'
)

html = html.replace(
    '<h4 class="font-bold text-lg mb-1">Punto Único de Verdad</h4>\n                                <p\n                                    class="text-cp-text-secondary dark:text-[theme(colors.cp.dark.text.secondary)] text-sm">\n                                    Centralización completa de expedientes digitales e historial de estudiantes.</p>',
    '<h4 class="font-bold text-lg mb-1">Orden y Control</h4>\n                                <p\n                                    class="text-cp-text-secondary dark:text-[theme(colors.cp.dark.text.secondary)] text-sm">\n                                    Información consolidada sin uso de papel y con rápido acceso para directivos.</p>'
)

# Replace titles of feature cards slightly if needed
html = html.replace('<h4 class="font-bold mb-2">Registro digital</h4>', '<h4 class="font-bold mb-2">Registro de incidentes</h4>')
html = html.replace('<h4 class="font-bold mb-2">Historial</h4>', '<h4 class="font-bold mb-2">Historial de alumnos</h4>')
html = html.replace('<h4 class="font-bold mb-2">Dashboard</h4>', '<h4 class="font-bold mb-2">Dashboard de estadísticas</h4>')
html = html.replace('<h4 class="font-bold mb-2">Seguimiento</h4>', '<h4 class="font-bold mb-2">Seguimiento de casos</h4>')
html = html.replace('<h4 class="font-bold mb-2">Roles</h4>', '<h4 class="font-bold mb-2">Roles de usuario</h4>')

# 5. Como Funciona
html = html.replace('<h4 class="font-bold mb-2 text-xl">Registrar</h4>\n                    <p class="text-sm text-white/80">Inicio rápido del caso digital.</p>', '<h4 class="font-bold mb-2 text-xl">Registrar incidente</h4>\n                    <p class="text-sm text-white/80">Crea el incidente en el sistema.</p>')
html = html.replace('<h4 class="font-bold mb-2 text-xl">Analizar</h4>\n                    <p class="text-sm text-white/80">Evaluación profesional del contexto.</p>', '<h4 class="font-bold mb-2 text-xl">Analizar caso</h4>\n                    <p class="text-sm text-white/80">Revisa el caso y sus antecedentes.</p>')
html = html.replace('<h4 class="font-bold mb-2 text-xl">Evidenciar</h4>\n                    <p class="text-sm text-white/80">Carga de respaldo multimedia.</p>', '<h4 class="font-bold mb-2 text-xl">Adjuntar evidencias</h4>\n                    <p class="text-sm text-white/80">Añade evidencias relevantes al caso.</p>')
html = html.replace('<h4 class="font-bold mb-2 text-xl">Actuar</h4>\n                    <p class="text-sm text-white/80">Aplicación de medidas y compromisos.</p>', '<h4 class="font-bold mb-2 text-xl">Aplicar medidas</h4>\n                    <p class="text-sm text-white/80">Dicta medidas disciplinarias.</p>')
html = html.replace('<h4 class="font-bold mb-2 text-xl">Medir</h4>\n                    <p class="text-sm text-white/80">Generación de informes automáticos.</p>', '<h4 class="font-bold mb-2 text-xl">Generar reportes</h4>\n                    <p class="text-sm text-white/80">Obtén reportes y estadísticas.</p>')

# 6. Beneficios (Overwriting the "Capturas" section text to become Benefits)
html = html.replace(
    '<span class="text-cp-accent font-bold tracking-wider uppercase text-sm mb-4 block">La Interfaz</span>\n                <h2 class="text-4xl md:text-5xl font-black mb-6">Experiencia de usuario fluida</h2>\n                <p class="text-xl text-cp-text-secondary dark:text-[theme(colors.cp.dark.text.secondary)]">Diseñado para\n                    ser intuitivo y eliminar la fricción administrativa.</p>',
    '<span class="text-cp-accent font-bold tracking-wider uppercase text-sm mb-4 block">Tus Beneficios</span>\n                <h2 class="text-4xl md:text-5xl font-black mb-6">¿Por qué elegir Convive+?</h2>\n                <p class="text-xl text-cp-text-secondary dark:text-[theme(colors.cp.dark.text.secondary)]">Convive+ transforma la gestión diaria de tu establecimiento en resultados medibles.</p>'
)

# Card 1 benefit
html = html.replace(
    '<span\n                                class="text-cp-text-inverse font-bold bg-cp-accent/90 px-4 py-2 rounded-full text-sm shadow-xl backdrop-blur-sm">Registro\n                                rápido e intuitivo</span>',
    '<span\n                                class="text-cp-text-inverse font-bold bg-cp-accent/90 px-4 py-2 rounded-full text-sm shadow-xl backdrop-blur-sm">Ahorro de tiempo</span>'
)
html = html.replace('<h4 class="font-bold text-xl text-center">Registro de Incidentes</h4>', '<h4 class="font-bold text-xl text-center">Mayor organización operativa</h4>')

# Card 2 benefit
html = html.replace(
    '<span\n                                class="text-cp-text-inverse font-bold bg-cp-accent/90 px-4 py-2 rounded-full text-sm shadow-xl backdrop-blur-sm">Métricas\n                                en tiempo real</span>',
    '<span\n                                class="text-cp-text-inverse font-bold bg-cp-accent/90 px-4 py-2 rounded-full text-sm shadow-xl backdrop-blur-sm">Información clara</span>'
)
html = html.replace('<h4 class="font-bold text-xl text-center">Dashboard General</h4>', '<h4 class="font-bold text-xl text-center">Decisiones informadas y transparencia</h4>')

# Card 3 benefit
html = html.replace(
    '<span\n                                class="text-cp-text-inverse font-bold bg-cp-accent/90 px-4 py-2 rounded-full text-sm shadow-xl backdrop-blur-sm">Trazabilidad\n                                completa</span>',
    '<span\n                                class="text-cp-text-inverse font-bold bg-cp-accent/90 px-4 py-2 rounded-full text-sm shadow-xl backdrop-blur-sm">Tracking total</span>'
)
html = html.replace('<h4 class="font-bold text-xl text-center">Perfil del Estudiante</h4>', '<h4 class="font-bold text-xl text-center">Seguimiento claro de casos</h4>')

# 7. Add School Logos snippet right after the Social Proof header
logos_html = """
            <!-- Logos Placeholders -->
            <div class="mb-20 text-center relative z-10 w-full overflow-hidden">
                <p class="text-sm font-bold text-cp-text-secondary dark:text-[theme(colors.cp.dark.text.secondary)] uppercase tracking-wider mb-8">Colegios que ya confían en Convive+</p>
                <div class="flex flex-wrap justify-center items-center gap-10 opacity-70 grayscale">
                    <div class="flex items-center gap-2"><span class="material-symbols-outlined text-4xl">school</span><span class="font-bold text-xl">Liceo Nacional</span></div>
                    <div class="flex items-center gap-2"><span class="material-symbols-outlined text-4xl">menu_book</span><span class="font-bold text-xl">Colegio San José</span></div>
                    <div class="flex items-center gap-2"><span class="material-symbols-outlined text-4xl">history_edu</span><span class="font-bold text-xl">Inst. Bicentenario</span></div>
                    <div class="flex items-center gap-2"><span class="material-symbols-outlined text-4xl">local_library</span><span class="font-bold text-xl">Colegio Altamira</span></div>
                </div>
            </div>
"""
html = html.replace('Colegios que ya transformaron su convivencia</h2>\n            </div>', f'Colegios que ya transformaron su convivencia</h2>\n            </div>\n{logos_html}')

# 8. Pricing Update
html = html.replace('Precios transparentes para todos', 'Planes adaptados a tu colegio')
html = html.replace('Soluciones\n                    escalables basadas en la matrícula de tu institución.', 'Ahorra con la opción anual. Selecciona el mejor plan para tu establecimiento.')

html = html.replace('<div class="mb-6 flex items-baseline gap-1">\n                        <span class="text-4xl font-black">Cotizar</span>\n                    </div>', '<div class="mb-6 flex items-baseline gap-1">\n                        <span class="text-4xl font-black">$39.990</span><span class="text-sm text-cp-text-secondary">/mes</span>\n                    </div>')
html = html.replace('Solicitar\n                        cotización', 'Contratar Plan Básico')

html = html.replace('<div class="mb-6 flex items-baseline gap-1">\n                        <span class="text-5xl font-black">UF 3</span>\n                        <span class="text-cp-brand-muted">/mes</span>\n                    </div>', '<div class="mb-6 flex items-baseline gap-1">\n                        <span class="text-4xl font-black">$69.990</span>\n                        <span class="text-cp-brand-muted">/mes</span>\n                    </div>')
html = html.replace('Más\n                            Popular', 'Plan más utilizado')

# The third plan is Corporativo with "Personalizado", change to Premium
html = html.replace('<h3 class="text-xl font-bold mb-2">Redes</h3>', '<h3 class="text-xl font-bold mb-2">Premium</h3>')
html = html.replace('Para\n                        múltiples colegios', 'Para colegios de alta exigencia')
html = html.replace('<div class="mb-6 flex items-baseline gap-1">\n                        <span class="text-4xl font-black">Personalizado</span>\n                    </div>', '<div class="mb-6 flex items-baseline gap-1">\n                        <span class="text-4xl font-black">$99.990</span><span class="text-sm text-cp-text-secondary">/mes</span>\n                    </div>')
html = html.replace('Hablar\n                        con ventas', 'Contratar Plan Premium')

# 9. CTA FINAL
html = html.replace('Transforma la gestión de convivencia hoy', 'Transforma la gestión de convivencia escolar en tu establecimiento')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
