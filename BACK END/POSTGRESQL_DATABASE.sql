PGDMP     "    1            	    {            hzndkfkd "   11.19 (Ubuntu 11.19-1.pgdg20.04+1)    15.2 �    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    17286911    hzndkfkd    DATABASE     t   CREATE DATABASE hzndkfkd WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.UTF-8';
    DROP DATABASE hzndkfkd;
                hzndkfkd    false            �           0    0    DATABASE hzndkfkd    ACL     ;   REVOKE CONNECT,TEMPORARY ON DATABASE hzndkfkd FROM PUBLIC;
                   hzndkfkd    false    4252                        2615    17286941    assessments    SCHEMA        CREATE SCHEMA assessments;
    DROP SCHEMA assessments;
                hzndkfkd    false                        2615    17286942    cargos    SCHEMA        CREATE SCHEMA cargos;
    DROP SCHEMA cargos;
                hzndkfkd    false                        2615    2200    public    SCHEMA     2   -- *not* creating schema, since initdb creates it
 2   -- *not* dropping schema, since initdb creates it
                postgres    false            �           0    0    SCHEMA public    ACL     Q   REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
                   postgres    false    27                        2615    17286943 
   respuestas    SCHEMA        CREATE SCHEMA respuestas;
    DROP SCHEMA respuestas;
                hzndkfkd    false                         2615    17286944    usuarios    SCHEMA        CREATE SCHEMA usuarios;
    DROP SCHEMA usuarios;
                hzndkfkd    false            	            3079    17135 	   btree_gin 	   EXTENSION     =   CREATE EXTENSION IF NOT EXISTS btree_gin WITH SCHEMA public;
    DROP EXTENSION btree_gin;
                   false    27            �           0    0    EXTENSION btree_gin    COMMENT     R   COMMENT ON EXTENSION btree_gin IS 'support for indexing common datatypes in GIN';
                        false    9                        3079    17680 
   btree_gist 	   EXTENSION     >   CREATE EXTENSION IF NOT EXISTS btree_gist WITH SCHEMA public;
    DROP EXTENSION btree_gist;
                   false    27            �           0    0    EXTENSION btree_gist    COMMENT     T   COMMENT ON EXTENSION btree_gist IS 'support for indexing common datatypes in GiST';
                        false    5                        3079    16661    citext 	   EXTENSION     :   CREATE EXTENSION IF NOT EXISTS citext WITH SCHEMA public;
    DROP EXTENSION citext;
                   false    27            �           0    0    EXTENSION citext    COMMENT     S   COMMENT ON EXTENSION citext IS 'data type for case-insensitive character strings';
                        false    16                        3079    17577    cube 	   EXTENSION     8   CREATE EXTENSION IF NOT EXISTS cube WITH SCHEMA public;
    DROP EXTENSION cube;
                   false    27            �           0    0    EXTENSION cube    COMMENT     E   COMMENT ON EXTENSION cube IS 'data type for multidimensional cubes';
                        false    7                        3079    16384    dblink 	   EXTENSION     :   CREATE EXTENSION IF NOT EXISTS dblink WITH SCHEMA public;
    DROP EXTENSION dblink;
                   false    27            �           0    0    EXTENSION dblink    COMMENT     _   COMMENT ON EXTENSION dblink IS 'connect to other PostgreSQL databases from within a database';
                        false    22            
            3079    17130    dict_int 	   EXTENSION     <   CREATE EXTENSION IF NOT EXISTS dict_int WITH SCHEMA public;
    DROP EXTENSION dict_int;
                   false    27            �           0    0    EXTENSION dict_int    COMMENT     Q   COMMENT ON EXTENSION dict_int IS 'text search dictionary template for integers';
                        false    10                        3079    18303 	   dict_xsyn 	   EXTENSION     =   CREATE EXTENSION IF NOT EXISTS dict_xsyn WITH SCHEMA public;
    DROP EXTENSION dict_xsyn;
                   false    27            �           0    0    EXTENSION dict_xsyn    COMMENT     e   COMMENT ON EXTENSION dict_xsyn IS 'text search dictionary template for extended synonym processing';
                        false    4                        3079    17664    earthdistance 	   EXTENSION     A   CREATE EXTENSION IF NOT EXISTS earthdistance WITH SCHEMA public;
    DROP EXTENSION earthdistance;
                   false    7    27            �           0    0    EXTENSION earthdistance    COMMENT     f   COMMENT ON EXTENSION earthdistance IS 'calculate great-circle distances on the surface of the Earth';
                        false    6                        3079    16650    fuzzystrmatch 	   EXTENSION     A   CREATE EXTENSION IF NOT EXISTS fuzzystrmatch WITH SCHEMA public;
    DROP EXTENSION fuzzystrmatch;
                   false    27            �           0    0    EXTENSION fuzzystrmatch    COMMENT     ]   COMMENT ON EXTENSION fuzzystrmatch IS 'determine similarities and distance between strings';
                        false    17                        3079    17007    hstore 	   EXTENSION     :   CREATE EXTENSION IF NOT EXISTS hstore WITH SCHEMA public;
    DROP EXTENSION hstore;
                   false    27            �           0    0    EXTENSION hstore    COMMENT     S   COMMENT ON EXTENSION hstore IS 'data type for storing sets of (key, value) pairs';
                        false    11                        3079    16889    intarray 	   EXTENSION     <   CREATE EXTENSION IF NOT EXISTS intarray WITH SCHEMA public;
    DROP EXTENSION intarray;
                   false    27            �           0    0    EXTENSION intarray    COMMENT     g   COMMENT ON EXTENSION intarray IS 'functions, operators, and index support for 1-D arrays of integers';
                        false    12                        3079    16444    ltree 	   EXTENSION     9   CREATE EXTENSION IF NOT EXISTS ltree WITH SCHEMA public;
    DROP EXTENSION ltree;
                   false    27            �           0    0    EXTENSION ltree    COMMENT     Q   COMMENT ON EXTENSION ltree IS 'data type for hierarchical tree-like structures';
                        false    20                        3079    18315    pg_stat_statements 	   EXTENSION     F   CREATE EXTENSION IF NOT EXISTS pg_stat_statements WITH SCHEMA public;
 #   DROP EXTENSION pg_stat_statements;
                   false    27            �           0    0    EXTENSION pg_stat_statements    COMMENT     h   COMMENT ON EXTENSION pg_stat_statements IS 'track execution statistics of all SQL statements executed';
                        false    2                        3079    16812    pg_trgm 	   EXTENSION     ;   CREATE EXTENSION IF NOT EXISTS pg_trgm WITH SCHEMA public;
    DROP EXTENSION pg_trgm;
                   false    27            �           0    0    EXTENSION pg_trgm    COMMENT     e   COMMENT ON EXTENSION pg_trgm IS 'text similarity measurement and index searching based on trigrams';
                        false    13                        3079    16775    pgcrypto 	   EXTENSION     <   CREATE EXTENSION IF NOT EXISTS pgcrypto WITH SCHEMA public;
    DROP EXTENSION pgcrypto;
                   false    27            �           0    0    EXTENSION pgcrypto    COMMENT     <   COMMENT ON EXTENSION pgcrypto IS 'cryptographic functions';
                        false    14                        3079    17571 
   pgrowlocks 	   EXTENSION     >   CREATE EXTENSION IF NOT EXISTS pgrowlocks WITH SCHEMA public;
    DROP EXTENSION pgrowlocks;
                   false    27            �           0    0    EXTENSION pgrowlocks    COMMENT     I   COMMENT ON EXTENSION pgrowlocks IS 'show row-level locking information';
                        false    8                        3079    16619    pgstattuple 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS pgstattuple WITH SCHEMA public;
    DROP EXTENSION pgstattuple;
                   false    27            �           0    0    EXTENSION pgstattuple    COMMENT     C   COMMENT ON EXTENSION pgstattuple IS 'show tuple-level statistics';
                        false    19                        3079    16629 	   tablefunc 	   EXTENSION     =   CREATE EXTENSION IF NOT EXISTS tablefunc WITH SCHEMA public;
    DROP EXTENSION tablefunc;
                   false    27            �           0    0    EXTENSION tablefunc    COMMENT     `   COMMENT ON EXTENSION tablefunc IS 'functions that manipulate whole tables, including crosstab';
                        false    18                        3079    18308    unaccent 	   EXTENSION     <   CREATE EXTENSION IF NOT EXISTS unaccent WITH SCHEMA public;
    DROP EXTENSION unaccent;
                   false    27            �           0    0    EXTENSION unaccent    COMMENT     P   COMMENT ON EXTENSION unaccent IS 'text search dictionary that removes accents';
                        false    3                        3079    16764 	   uuid-ossp 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;
    DROP EXTENSION "uuid-ossp";
                   false    27            �           0    0    EXTENSION "uuid-ossp"    COMMENT     W   COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';
                        false    15                        3079    16430    xml2 	   EXTENSION     8   CREATE EXTENSION IF NOT EXISTS xml2 WITH SCHEMA public;
    DROP EXTENSION xml2;
                   false    27            �           0    0    EXTENSION xml2    COMMENT     8   COMMENT ON EXTENSION xml2 IS 'XPath querying and XSLT';
                        false    21            �            1259    17286945    assessments    TABLE     e  CREATE TABLE assessments.assessments (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombre character varying NOT NULL,
    descripcion character varying,
    es_plantilla boolean DEFAULT false,
    id_usuario_administrador uuid NOT NULL,
    eliminado boolean DEFAULT false,
    fecha_de_registro timestamp without time zone DEFAULT now()
);
 $   DROP TABLE assessments.assessments;
       assessments            hzndkfkd    false    15    27    29            �            1259    17286955    avatares_virtuales    TABLE     �  CREATE TABLE assessments.avatares_virtuales (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombre character varying NOT NULL,
    id_cuenta_sitepal character varying,
    id_escena_sitepal character varying,
    id_embed_sitepal character varying,
    voz character varying,
    lenguaje character varying,
    motor character varying,
    eliminado boolean DEFAULT false,
    fecha_de_registro timestamp without time zone DEFAULT now()
);
 +   DROP TABLE assessments.avatares_virtuales;
       assessments            hzndkfkd    false    15    27    29            �            1259    17286964    competencias    TABLE     >  CREATE TABLE assessments.competencias (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombre character varying NOT NULL,
    descripcion character varying,
    eliminado boolean DEFAULT false,
    fecha_de_registro timestamp without time zone DEFAULT now(),
    id_usuario_administrador uuid NOT NULL
);
 %   DROP TABLE assessments.competencias;
       assessments            hzndkfkd    false    15    27    29            �            1259    17286973    competencias_assessments    TABLE       CREATE TABLE assessments.competencias_assessments (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    id_assessment uuid NOT NULL,
    id_competencia uuid NOT NULL,
    eliminado boolean DEFAULT false,
    fecha_de_registro timestamp without time zone DEFAULT now()
);
 1   DROP TABLE assessments.competencias_assessments;
       assessments            hzndkfkd    false    15    27    29            �            1259    17286979    descarriladores    TABLE       CREATE TABLE assessments.descarriladores (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    descarrilador character varying(100) NOT NULL,
    id_pregunta uuid NOT NULL,
    eliminado boolean DEFAULT false,
    fecha_de_registro timestamp without time zone DEFAULT now()
);
 (   DROP TABLE assessments.descarriladores;
       assessments            hzndkfkd    false    15    27    29            �            1259    17286985    momentos    TABLE     ;  CREATE TABLE assessments.momentos (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombre character varying NOT NULL,
    descripcion character varying,
    id_competencia_assessment uuid NOT NULL,
    eliminado boolean DEFAULT false,
    fecha_de_registro timestamp without time zone DEFAULT now()
);
 !   DROP TABLE assessments.momentos;
       assessments            hzndkfkd    false    15    27    29            �            1259    17286994    palabras_clave    TABLE       CREATE TABLE assessments.palabras_clave (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    palabra character varying(100) NOT NULL,
    id_pregunta uuid NOT NULL,
    eliminado boolean DEFAULT false,
    fecha_de_registro timestamp without time zone DEFAULT now()
);
 '   DROP TABLE assessments.palabras_clave;
       assessments            hzndkfkd    false    15    27    29            �            1259    17287000 	   preguntas    TABLE     �  CREATE TABLE assessments.preguntas (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    id_momento uuid NOT NULL,
    pregunta character varying NOT NULL,
    texto_avatar character varying,
    respuesta_sugerida character varying,
    umbral_minimo_calificacion numeric,
    umbral_maximo_calificacion numeric,
    duracion_maxima_de_respuesta integer,
    id_parametro_tipo_avatar uuid,
    video_avatar_pregunta character varying,
    id_avatar_virtual uuid,
    nombre_avatar character varying,
    peso_calificacion_evaluador integer,
    peso_calificacion_ia integer,
    calificacion_con_ia boolean,
    eliminado boolean DEFAULT false,
    fecha_de_registro timestamp without time zone DEFAULT now()
);
 "   DROP TABLE assessments.preguntas;
       assessments            hzndkfkd    false    15    27    29            �            1259    17287009    cargos    TABLE     �  CREATE TABLE cargos.cargos (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombre character varying NOT NULL,
    titulo_profesional_requerido character varying,
    minimo_salario_mensual numeric,
    maximo_salario_mensual numeric,
    id_parametro_moneda uuid,
    ubicacion character varying,
    trabajo_remoto boolean,
    descripcion character varying,
    requisitos character varying,
    proceso_de_contratacion character varying,
    id_assessment uuid,
    id_usuario_administrador uuid NOT NULL,
    publicado boolean DEFAULT false,
    eliminado boolean DEFAULT false,
    fecha_de_registro timestamp without time zone DEFAULT now(),
    vacantes integer DEFAULT 1,
    empresa_oferente character varying
);
    DROP TABLE cargos.cargos;
       cargos            hzndkfkd    false    15    27    30            �            1259    17795511    postulaciones    TABLE       CREATE TABLE cargos.postulaciones (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    id_usuario_candidato uuid NOT NULL,
    id_cargo uuid NOT NULL,
    id_assessment uuid,
    id_parametro_estado_de_postulacion_candidato uuid,
    eliminado boolean DEFAULT false,
    fecha_de_registro timestamp without time zone DEFAULT now(),
    calificacion_final character varying,
    observaciones_finales character varying,
    mensaje_final_para_candidato character varying,
    observaciones_finales_ia character varying
);
 !   DROP TABLE cargos.postulaciones;
       cargos            hzndkfkd    false    15    27    30            �            1259    17287020 
   parametros    TABLE     '  CREATE TABLE public.parametros (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombre character varying,
    descripcion character varying,
    id_tipo_parametro uuid NOT NULL,
    eliminado boolean DEFAULT false,
    fecha_de_registro timestamp without time zone DEFAULT now()
);
    DROP TABLE public.parametros;
       public            hzndkfkd    false    15    27    27            �            1259    17287029    tipos_parametros    TABLE       CREATE TABLE public.tipos_parametros (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombre character varying NOT NULL,
    descripcion character varying,
    eliminado boolean DEFAULT false,
    fecha_de_registro timestamp without time zone DEFAULT now()
);
 $   DROP TABLE public.tipos_parametros;
       public            hzndkfkd    false    15    27    27            �            1259    17287038    evaluaciones_respuestas    TABLE     0  CREATE TABLE respuestas.evaluaciones_respuestas (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    id_respuesta_candidato uuid NOT NULL,
    calificacion_de_ia character varying,
    observaciones_de_ia character varying,
    calificacion_del_evaluador character varying,
    observaciones_del_evaluador character varying,
    porcentaje_coincidencia_con_respuesta_correcta character varying,
    promedio_de_calificacion character varying,
    porcentaje_calificacion_ia numeric DEFAULT 0,
    porcentaje_calificacion_evaluador numeric DEFAULT 100,
    transcripcion_respuesta character varying,
    emocion_prevalente character varying,
    data_emociones jsonb,
    respuesta_ia character varying,
    eliminado boolean DEFAULT false,
    fecha_de_registro timestamp without time zone DEFAULT now()
);
 /   DROP TABLE respuestas.evaluaciones_respuestas;
    
   respuestas            hzndkfkd    false    15    27    31            �            1259    17287049    respuestas_candidatos    TABLE     _  CREATE TABLE respuestas.respuestas_candidatos (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    id_usuario_candidato uuid NOT NULL,
    id_pregunta uuid NOT NULL,
    video_respuesta_usuario character varying,
    eliminado boolean DEFAULT false,
    fecha_de_registro timestamp without time zone DEFAULT now(),
    data_emociones json
);
 -   DROP TABLE respuestas.respuestas_candidatos;
    
   respuestas            hzndkfkd    false    15    27    31            �            1259    17287058     tokens_de_acceso_administradores    TABLE     a  CREATE TABLE usuarios.tokens_de_acceso_administradores (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    token_administrador character varying,
    id_usuario_administrador uuid NOT NULL,
    fecha_caducidad timestamp without time zone,
    fecha_de_registro timestamp without time zone DEFAULT now(),
    eliminado boolean DEFAULT false
);
 6   DROP TABLE usuarios.tokens_de_acceso_administradores;
       usuarios            hzndkfkd    false    15    27    32            �            1259    17287067    tokens_de_acceso_candidatos    TABLE     T  CREATE TABLE usuarios.tokens_de_acceso_candidatos (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    token_candidato character varying,
    id_usuario_candidato uuid NOT NULL,
    fecha_caducidad timestamp without time zone,
    fecha_de_registro timestamp without time zone DEFAULT now(),
    eliminado boolean DEFAULT false
);
 1   DROP TABLE usuarios.tokens_de_acceso_candidatos;
       usuarios            hzndkfkd    false    15    27    32            �            1259    17287076    usuarios_administradores    TABLE     H  CREATE TABLE usuarios.usuarios_administradores (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombres character varying NOT NULL,
    apellidos character varying,
    correo character varying NOT NULL,
    clave character varying,
    telefono character varying,
    id_parametro_pais uuid,
    fecha_de_nacimiento date,
    id_parametro_genero uuid,
    empresa character varying,
    foto_de_perfil character varying,
    descripcion_de_perfil character varying,
    eliminado boolean DEFAULT false,
    fecha_de_registro timestamp without time zone DEFAULT now()
);
 .   DROP TABLE usuarios.usuarios_administradores;
       usuarios            hzndkfkd    false    15    27    32            �            1259    17287085    usuarios_candidatos    TABLE     �  CREATE TABLE usuarios.usuarios_candidatos (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombres character varying NOT NULL,
    apellidos character varying,
    correo character varying NOT NULL,
    clave character varying,
    telefono character varying,
    id_parametro_pais uuid,
    fecha_de_nacimiento date,
    id_parametro_genero uuid,
    foto_de_perfil character varying,
    descripcion_perfil_usuario character varying,
    id_parametro_nivel_de_estudios uuid,
    id_parametro_anos_de_experiencia uuid,
    eliminado boolean DEFAULT false,
    fecha_de_registro timestamp without time zone DEFAULT now(),
    titulo_profesional character varying,
    hoja_de_vida character varying
);
 )   DROP TABLE usuarios.usuarios_candidatos;
       usuarios            hzndkfkd    false    15    27    32            �          0    17286945    assessments 
   TABLE DATA           �   COPY assessments.assessments (id, nombre, descripcion, es_plantilla, id_usuario_administrador, eliminado, fecha_de_registro) FROM stdin;
    assessments          hzndkfkd    false    226   ��       �          0    17286955    avatares_virtuales 
   TABLE DATA           �   COPY assessments.avatares_virtuales (id, nombre, id_cuenta_sitepal, id_escena_sitepal, id_embed_sitepal, voz, lenguaje, motor, eliminado, fecha_de_registro) FROM stdin;
    assessments          hzndkfkd    false    227   ��       �          0    17286964    competencias 
   TABLE DATA           |   COPY assessments.competencias (id, nombre, descripcion, eliminado, fecha_de_registro, id_usuario_administrador) FROM stdin;
    assessments          hzndkfkd    false    228   ��       �          0    17286973    competencias_assessments 
   TABLE DATA           x   COPY assessments.competencias_assessments (id, id_assessment, id_competencia, eliminado, fecha_de_registro) FROM stdin;
    assessments          hzndkfkd    false    229   ��       �          0    17286979    descarriladores 
   TABLE DATA           l   COPY assessments.descarriladores (id, descarrilador, id_pregunta, eliminado, fecha_de_registro) FROM stdin;
    assessments          hzndkfkd    false    230   e�       �          0    17286985    momentos 
   TABLE DATA           y   COPY assessments.momentos (id, nombre, descripcion, id_competencia_assessment, eliminado, fecha_de_registro) FROM stdin;
    assessments          hzndkfkd    false    231   ��       �          0    17286994    palabras_clave 
   TABLE DATA           e   COPY assessments.palabras_clave (id, palabra, id_pregunta, eliminado, fecha_de_registro) FROM stdin;
    assessments          hzndkfkd    false    232   �       �          0    17287000 	   preguntas 
   TABLE DATA           s  COPY assessments.preguntas (id, id_momento, pregunta, texto_avatar, respuesta_sugerida, umbral_minimo_calificacion, umbral_maximo_calificacion, duracion_maxima_de_respuesta, id_parametro_tipo_avatar, video_avatar_pregunta, id_avatar_virtual, nombre_avatar, peso_calificacion_evaluador, peso_calificacion_ia, calificacion_con_ia, eliminado, fecha_de_registro) FROM stdin;
    assessments          hzndkfkd    false    233   ��       �          0    17287009    cargos 
   TABLE DATA           J  COPY cargos.cargos (id, nombre, titulo_profesional_requerido, minimo_salario_mensual, maximo_salario_mensual, id_parametro_moneda, ubicacion, trabajo_remoto, descripcion, requisitos, proceso_de_contratacion, id_assessment, id_usuario_administrador, publicado, eliminado, fecha_de_registro, vacantes, empresa_oferente) FROM stdin;
    cargos          hzndkfkd    false    234   �       �          0    17795511    postulaciones 
   TABLE DATA           	  COPY cargos.postulaciones (id, id_usuario_candidato, id_cargo, id_assessment, id_parametro_estado_de_postulacion_candidato, eliminado, fecha_de_registro, calificacion_final, observaciones_finales, mensaje_final_para_candidato, observaciones_finales_ia) FROM stdin;
    cargos          hzndkfkd    false    243   �      �          0    17287020 
   parametros 
   TABLE DATA           n   COPY public.parametros (id, nombre, descripcion, id_tipo_parametro, eliminado, fecha_de_registro) FROM stdin;
    public          hzndkfkd    false    235   �      �          0    17287029    tipos_parametros 
   TABLE DATA           a   COPY public.tipos_parametros (id, nombre, descripcion, eliminado, fecha_de_registro) FROM stdin;
    public          hzndkfkd    false    236   V$      �          0    17287038    evaluaciones_respuestas 
   TABLE DATA           �  COPY respuestas.evaluaciones_respuestas (id, id_respuesta_candidato, calificacion_de_ia, observaciones_de_ia, calificacion_del_evaluador, observaciones_del_evaluador, porcentaje_coincidencia_con_respuesta_correcta, promedio_de_calificacion, porcentaje_calificacion_ia, porcentaje_calificacion_evaluador, transcripcion_respuesta, emocion_prevalente, data_emociones, respuesta_ia, eliminado, fecha_de_registro) FROM stdin;
 
   respuestas          hzndkfkd    false    237   �&      �          0    17287049    respuestas_candidatos 
   TABLE DATA           �   COPY respuestas.respuestas_candidatos (id, id_usuario_candidato, id_pregunta, video_respuesta_usuario, eliminado, fecha_de_registro, data_emociones) FROM stdin;
 
   respuestas          hzndkfkd    false    238   ��      �          0    17287058     tokens_de_acceso_administradores 
   TABLE DATA           �   COPY usuarios.tokens_de_acceso_administradores (id, token_administrador, id_usuario_administrador, fecha_caducidad, fecha_de_registro, eliminado) FROM stdin;
    usuarios          hzndkfkd    false    239   Ua      �          0    17287067    tokens_de_acceso_candidatos 
   TABLE DATA           �   COPY usuarios.tokens_de_acceso_candidatos (id, token_candidato, id_usuario_candidato, fecha_caducidad, fecha_de_registro, eliminado) FROM stdin;
    usuarios          hzndkfkd    false    240   ra      �          0    17287076    usuarios_administradores 
   TABLE DATA           �   COPY usuarios.usuarios_administradores (id, nombres, apellidos, correo, clave, telefono, id_parametro_pais, fecha_de_nacimiento, id_parametro_genero, empresa, foto_de_perfil, descripcion_de_perfil, eliminado, fecha_de_registro) FROM stdin;
    usuarios          hzndkfkd    false    241   �a      �          0    17287085    usuarios_candidatos 
   TABLE DATA           K  COPY usuarios.usuarios_candidatos (id, nombres, apellidos, correo, clave, telefono, id_parametro_pais, fecha_de_nacimiento, id_parametro_genero, foto_de_perfil, descripcion_perfil_usuario, id_parametro_nivel_de_estudios, id_parametro_anos_de_experiencia, eliminado, fecha_de_registro, titulo_profesional, hoja_de_vida) FROM stdin;
    usuarios          hzndkfkd    false    242   me      �           2606    17287095 4   competencias_assessments pk_competencias_assessments 
   CONSTRAINT     w   ALTER TABLE ONLY assessments.competencias_assessments
    ADD CONSTRAINT pk_competencias_assessments PRIMARY KEY (id);
 c   ALTER TABLE ONLY assessments.competencias_assessments DROP CONSTRAINT pk_competencias_assessments;
       assessments            hzndkfkd    false    229            �           2606    17797757    assessments pk_id_assessment 
   CONSTRAINT     l   ALTER TABLE ONLY assessments.assessments
    ADD CONSTRAINT pk_id_assessment PRIMARY KEY (id) INCLUDE (id);
 K   ALTER TABLE ONLY assessments.assessments DROP CONSTRAINT pk_id_assessment;
       assessments            hzndkfkd    false    226    226            �           2606    17287099 '   avatares_virtuales pk_id_avatar_virtual 
   CONSTRAINT     n   ALTER TABLE ONLY assessments.avatares_virtuales
    ADD CONSTRAINT pk_id_avatar_virtual PRIMARY KEY (nombre);
 V   ALTER TABLE ONLY assessments.avatares_virtuales DROP CONSTRAINT pk_id_avatar_virtual;
       assessments            hzndkfkd    false    227            �           2606    17287101    competencias pk_id_competencia 
   CONSTRAINT     a   ALTER TABLE ONLY assessments.competencias
    ADD CONSTRAINT pk_id_competencia PRIMARY KEY (id);
 M   ALTER TABLE ONLY assessments.competencias DROP CONSTRAINT pk_id_competencia;
       assessments            hzndkfkd    false    228            �           2606    17287103 #   descarriladores pk_id_descarrilador 
   CONSTRAINT     f   ALTER TABLE ONLY assessments.descarriladores
    ADD CONSTRAINT pk_id_descarrilador PRIMARY KEY (id);
 R   ALTER TABLE ONLY assessments.descarriladores DROP CONSTRAINT pk_id_descarrilador;
       assessments            hzndkfkd    false    230            �           2606    17811742    momentos pk_id_momento 
   CONSTRAINT     f   ALTER TABLE ONLY assessments.momentos
    ADD CONSTRAINT pk_id_momento PRIMARY KEY (id) INCLUDE (id);
 E   ALTER TABLE ONLY assessments.momentos DROP CONSTRAINT pk_id_momento;
       assessments            hzndkfkd    false    231    231            �           2606    17813171    preguntas pk_id_pregunta 
   CONSTRAINT     h   ALTER TABLE ONLY assessments.preguntas
    ADD CONSTRAINT pk_id_pregunta PRIMARY KEY (id) INCLUDE (id);
 G   ALTER TABLE ONLY assessments.preguntas DROP CONSTRAINT pk_id_pregunta;
       assessments            hzndkfkd    false    233    233            �           2606    17287109    palabras_clave pk_palabra_clave 
   CONSTRAINT     b   ALTER TABLE ONLY assessments.palabras_clave
    ADD CONSTRAINT pk_palabra_clave PRIMARY KEY (id);
 N   ALTER TABLE ONLY assessments.palabras_clave DROP CONSTRAINT pk_palabra_clave;
       assessments            hzndkfkd    false    232            �           2606    17287111    assessments u_id_assessment 
   CONSTRAINT     Y   ALTER TABLE ONLY assessments.assessments
    ADD CONSTRAINT u_id_assessment UNIQUE (id);
 J   ALTER TABLE ONLY assessments.assessments DROP CONSTRAINT u_id_assessment;
       assessments            hzndkfkd    false    226            �           2606    17287113 &   avatares_virtuales u_id_avatar_virtual 
   CONSTRAINT     d   ALTER TABLE ONLY assessments.avatares_virtuales
    ADD CONSTRAINT u_id_avatar_virtual UNIQUE (id);
 U   ALTER TABLE ONLY assessments.avatares_virtuales DROP CONSTRAINT u_id_avatar_virtual;
       assessments            hzndkfkd    false    227            �           2606    17287115    momentos u_id_momento 
   CONSTRAINT     S   ALTER TABLE ONLY assessments.momentos
    ADD CONSTRAINT u_id_momento UNIQUE (id);
 D   ALTER TABLE ONLY assessments.momentos DROP CONSTRAINT u_id_momento;
       assessments            hzndkfkd    false    231            �           2606    17287117    preguntas u_id_pregunta 
   CONSTRAINT     U   ALTER TABLE ONLY assessments.preguntas
    ADD CONSTRAINT u_id_pregunta UNIQUE (id);
 F   ALTER TABLE ONLY assessments.preguntas DROP CONSTRAINT u_id_pregunta;
       assessments            hzndkfkd    false    233            �           2606    17287119    cargos pk_id_cargo 
   CONSTRAINT     P   ALTER TABLE ONLY cargos.cargos
    ADD CONSTRAINT pk_id_cargo PRIMARY KEY (id);
 <   ALTER TABLE ONLY cargos.cargos DROP CONSTRAINT pk_id_cargo;
       cargos            hzndkfkd    false    234            �           2606    17795559    postulaciones pk_postulaciones 
   CONSTRAINT     i   ALTER TABLE ONLY cargos.postulaciones
    ADD CONSTRAINT pk_postulaciones PRIMARY KEY (id) INCLUDE (id);
 H   ALTER TABLE ONLY cargos.postulaciones DROP CONSTRAINT pk_postulaciones;
       cargos            hzndkfkd    false    243    243            �           2606    17287121    parametros pk_id_parametro 
   CONSTRAINT     X   ALTER TABLE ONLY public.parametros
    ADD CONSTRAINT pk_id_parametro PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.parametros DROP CONSTRAINT pk_id_parametro;
       public            hzndkfkd    false    235            �           2606    17287123 %   tipos_parametros pk_id_tipo_parametro 
   CONSTRAINT     c   ALTER TABLE ONLY public.tipos_parametros
    ADD CONSTRAINT pk_id_tipo_parametro PRIMARY KEY (id);
 O   ALTER TABLE ONLY public.tipos_parametros DROP CONSTRAINT pk_id_tipo_parametro;
       public            hzndkfkd    false    236            �           2606    17837338 2   evaluaciones_respuestas pk_id_evaluacion_respuesta 
   CONSTRAINT     t   ALTER TABLE ONLY respuestas.evaluaciones_respuestas
    ADD CONSTRAINT pk_id_evaluacion_respuesta PRIMARY KEY (id);
 `   ALTER TABLE ONLY respuestas.evaluaciones_respuestas DROP CONSTRAINT pk_id_evaluacion_respuesta;
    
   respuestas            hzndkfkd    false    237            �           2606    17287127 %   respuestas_candidatos pk_id_respuesta 
   CONSTRAINT     g   ALTER TABLE ONLY respuestas.respuestas_candidatos
    ADD CONSTRAINT pk_id_respuesta PRIMARY KEY (id);
 S   ALTER TABLE ONLY respuestas.respuestas_candidatos DROP CONSTRAINT pk_id_respuesta;
    
   respuestas            hzndkfkd    false    238            �           2606    17287129 1   evaluaciones_respuestas u_id_evaluacion_respuesta 
   CONSTRAINT     n   ALTER TABLE ONLY respuestas.evaluaciones_respuestas
    ADD CONSTRAINT u_id_evaluacion_respuesta UNIQUE (id);
 _   ALTER TABLE ONLY respuestas.evaluaciones_respuestas DROP CONSTRAINT u_id_evaluacion_respuesta;
    
   respuestas            hzndkfkd    false    237            �           2606    17837340 E   evaluaciones_respuestas u_id_respuesta_candidato_evaluacion_respuesta 
   CONSTRAINT     �   ALTER TABLE ONLY respuestas.evaluaciones_respuestas
    ADD CONSTRAINT u_id_respuesta_candidato_evaluacion_respuesta UNIQUE (id_respuesta_candidato);
 s   ALTER TABLE ONLY respuestas.evaluaciones_respuestas DROP CONSTRAINT u_id_respuesta_candidato_evaluacion_respuesta;
    
   respuestas            hzndkfkd    false    237            �           2606    17287131 :   tokens_de_acceso_administradores pk_id_token_administrador 
   CONSTRAINT     z   ALTER TABLE ONLY usuarios.tokens_de_acceso_administradores
    ADD CONSTRAINT pk_id_token_administrador PRIMARY KEY (id);
 f   ALTER TABLE ONLY usuarios.tokens_de_acceso_administradores DROP CONSTRAINT pk_id_token_administrador;
       usuarios            hzndkfkd    false    239            �           2606    17287133 1   tokens_de_acceso_candidatos pk_id_token_candidato 
   CONSTRAINT     q   ALTER TABLE ONLY usuarios.tokens_de_acceso_candidatos
    ADD CONSTRAINT pk_id_token_candidato PRIMARY KEY (id);
 ]   ALTER TABLE ONLY usuarios.tokens_de_acceso_candidatos DROP CONSTRAINT pk_id_token_candidato;
       usuarios            hzndkfkd    false    240            �           2606    17287135 4   usuarios_administradores pk_id_usuario_administrador 
   CONSTRAINT     t   ALTER TABLE ONLY usuarios.usuarios_administradores
    ADD CONSTRAINT pk_id_usuario_administrador PRIMARY KEY (id);
 `   ALTER TABLE ONLY usuarios.usuarios_administradores DROP CONSTRAINT pk_id_usuario_administrador;
       usuarios            hzndkfkd    false    241            �           2606    17287137 +   usuarios_candidatos pk_id_usuario_candidato 
   CONSTRAINT     k   ALTER TABLE ONLY usuarios.usuarios_candidatos
    ADD CONSTRAINT pk_id_usuario_candidato PRIMARY KEY (id);
 W   ALTER TABLE ONLY usuarios.usuarios_candidatos DROP CONSTRAINT pk_id_usuario_candidato;
       usuarios            hzndkfkd    false    242            �           2606    17287139 7   usuarios_administradores u_correo_usuario_administrador 
   CONSTRAINT     v   ALTER TABLE ONLY usuarios.usuarios_administradores
    ADD CONSTRAINT u_correo_usuario_administrador UNIQUE (correo);
 c   ALTER TABLE ONLY usuarios.usuarios_administradores DROP CONSTRAINT u_correo_usuario_administrador;
       usuarios            hzndkfkd    false    241            �           2606    17287141 .   usuarios_candidatos u_correo_usuario_candidato 
   CONSTRAINT     m   ALTER TABLE ONLY usuarios.usuarios_candidatos
    ADD CONSTRAINT u_correo_usuario_candidato UNIQUE (correo);
 Z   ALTER TABLE ONLY usuarios.usuarios_candidatos DROP CONSTRAINT u_correo_usuario_candidato;
       usuarios            hzndkfkd    false    242            �           2606    17287143 6   tokens_de_acceso_administradores u_token_administrador 
   CONSTRAINT     �   ALTER TABLE ONLY usuarios.tokens_de_acceso_administradores
    ADD CONSTRAINT u_token_administrador UNIQUE (token_administrador);
 b   ALTER TABLE ONLY usuarios.tokens_de_acceso_administradores DROP CONSTRAINT u_token_administrador;
       usuarios            hzndkfkd    false    239            �           2606    17287145 -   tokens_de_acceso_candidatos u_token_candidato 
   CONSTRAINT     u   ALTER TABLE ONLY usuarios.tokens_de_acceso_candidatos
    ADD CONSTRAINT u_token_candidato UNIQUE (token_candidato);
 Y   ALTER TABLE ONLY usuarios.tokens_de_acceso_candidatos DROP CONSTRAINT u_token_candidato;
       usuarios            hzndkfkd    false    240            �           2606    17287146 @   competencias_assessments fk_id_assessment_competencia_assessment    FK CONSTRAINT     �   ALTER TABLE ONLY assessments.competencias_assessments
    ADD CONSTRAINT fk_id_assessment_competencia_assessment FOREIGN KEY (id_assessment) REFERENCES assessments.assessments(id) NOT VALID;
 o   ALTER TABLE ONLY assessments.competencias_assessments DROP CONSTRAINT fk_id_assessment_competencia_assessment;
       assessments          hzndkfkd    false    226    4025    229            �           2606    17287151 '   preguntas fk_id_avatar_virtual_pregunta    FK CONSTRAINT     �   ALTER TABLE ONLY assessments.preguntas
    ADD CONSTRAINT fk_id_avatar_virtual_pregunta FOREIGN KEY (id_avatar_virtual) REFERENCES assessments.avatares_virtuales(id) NOT VALID;
 V   ALTER TABLE ONLY assessments.preguntas DROP CONSTRAINT fk_id_avatar_virtual_pregunta;
       assessments          hzndkfkd    false    4029    233    227            �           2606    17287156 -   momentos fk_id_competencia_assessment_momento    FK CONSTRAINT     �   ALTER TABLE ONLY assessments.momentos
    ADD CONSTRAINT fk_id_competencia_assessment_momento FOREIGN KEY (id_competencia_assessment) REFERENCES assessments.competencias_assessments(id) NOT VALID;
 \   ALTER TABLE ONLY assessments.momentos DROP CONSTRAINT fk_id_competencia_assessment_momento;
       assessments          hzndkfkd    false    229    4033    231            �           2606    17287161 A   competencias_assessments fk_id_competencia_competencia_assessment    FK CONSTRAINT     �   ALTER TABLE ONLY assessments.competencias_assessments
    ADD CONSTRAINT fk_id_competencia_competencia_assessment FOREIGN KEY (id_competencia) REFERENCES assessments.competencias(id) NOT VALID;
 p   ALTER TABLE ONLY assessments.competencias_assessments DROP CONSTRAINT fk_id_competencia_competencia_assessment;
       assessments          hzndkfkd    false    228    4031    229            �           2606    17287166     preguntas fk_id_momento_pregunta    FK CONSTRAINT     �   ALTER TABLE ONLY assessments.preguntas
    ADD CONSTRAINT fk_id_momento_pregunta FOREIGN KEY (id_momento) REFERENCES assessments.momentos(id) NOT VALID;
 O   ALTER TABLE ONLY assessments.preguntas DROP CONSTRAINT fk_id_momento_pregunta;
       assessments          hzndkfkd    false    233    4039    231            �           2606    17287171 .   preguntas fk_id_parametro_tipo_avatar_pregunta    FK CONSTRAINT     �   ALTER TABLE ONLY assessments.preguntas
    ADD CONSTRAINT fk_id_parametro_tipo_avatar_pregunta FOREIGN KEY (id_parametro_tipo_avatar) REFERENCES public.parametros(id) NOT VALID;
 ]   ALTER TABLE ONLY assessments.preguntas DROP CONSTRAINT fk_id_parametro_tipo_avatar_pregunta;
       assessments          hzndkfkd    false    4049    235    233            �           2606    17287176 ,   descarriladores fk_id_pregunta_descarrilador    FK CONSTRAINT     �   ALTER TABLE ONLY assessments.descarriladores
    ADD CONSTRAINT fk_id_pregunta_descarrilador FOREIGN KEY (id_pregunta) REFERENCES assessments.preguntas(id) NOT VALID;
 [   ALTER TABLE ONLY assessments.descarriladores DROP CONSTRAINT fk_id_pregunta_descarrilador;
       assessments          hzndkfkd    false    233    4045    230            �           2606    17287181 +   palabras_clave fk_id_pregunta_palabra_clave    FK CONSTRAINT     �   ALTER TABLE ONLY assessments.palabras_clave
    ADD CONSTRAINT fk_id_pregunta_palabra_clave FOREIGN KEY (id_pregunta) REFERENCES assessments.preguntas(id) NOT VALID;
 Z   ALTER TABLE ONLY assessments.palabras_clave DROP CONSTRAINT fk_id_pregunta_palabra_clave;
       assessments          hzndkfkd    false    233    4045    232            �           2606    17287186 2   assessments fk_id_usuario_administrador_assessment    FK CONSTRAINT     �   ALTER TABLE ONLY assessments.assessments
    ADD CONSTRAINT fk_id_usuario_administrador_assessment FOREIGN KEY (id_usuario_administrador) REFERENCES usuarios.usuarios_administradores(id) NOT VALID;
 a   ALTER TABLE ONLY assessments.assessments DROP CONSTRAINT fk_id_usuario_administrador_assessment;
       assessments          hzndkfkd    false    4069    241    226            �           2606    17785784 4   competencias fk_id_usuario_administrador_competencia    FK CONSTRAINT     �   ALTER TABLE ONLY assessments.competencias
    ADD CONSTRAINT fk_id_usuario_administrador_competencia FOREIGN KEY (id_usuario_administrador) REFERENCES usuarios.usuarios_administradores(id) NOT VALID;
 c   ALTER TABLE ONLY assessments.competencias DROP CONSTRAINT fk_id_usuario_administrador_competencia;
       assessments          hzndkfkd    false    241    4069    228            �           2606    17287191    cargos fk_id_assessment_cargo    FK CONSTRAINT     �   ALTER TABLE ONLY cargos.cargos
    ADD CONSTRAINT fk_id_assessment_cargo FOREIGN KEY (id_assessment) REFERENCES assessments.assessments(id) NOT VALID;
 G   ALTER TABLE ONLY cargos.cargos DROP CONSTRAINT fk_id_assessment_cargo;
       cargos          hzndkfkd    false    234    226    4025                       2606    17795570 *   postulaciones fk_id_assessment_postulacion    FK CONSTRAINT     �   ALTER TABLE ONLY cargos.postulaciones
    ADD CONSTRAINT fk_id_assessment_postulacion FOREIGN KEY (id_assessment) REFERENCES assessments.assessments(id) NOT VALID;
 T   ALTER TABLE ONLY cargos.postulaciones DROP CONSTRAINT fk_id_assessment_postulacion;
       cargos          hzndkfkd    false    243    4025    226                       2606    17795565 %   postulaciones fk_id_cargo_postulacion    FK CONSTRAINT     �   ALTER TABLE ONLY cargos.postulaciones
    ADD CONSTRAINT fk_id_cargo_postulacion FOREIGN KEY (id_cargo) REFERENCES cargos.cargos(id) NOT VALID;
 O   ALTER TABLE ONLY cargos.postulaciones DROP CONSTRAINT fk_id_cargo_postulacion;
       cargos          hzndkfkd    false    243    4047    234            	           2606    17795575 I   postulaciones fk_id_parametro_estado_de_postulacion_candidato_postulacion    FK CONSTRAINT     �   ALTER TABLE ONLY cargos.postulaciones
    ADD CONSTRAINT fk_id_parametro_estado_de_postulacion_candidato_postulacion FOREIGN KEY (id_parametro_estado_de_postulacion_candidato) REFERENCES public.parametros(id) NOT VALID;
 s   ALTER TABLE ONLY cargos.postulaciones DROP CONSTRAINT fk_id_parametro_estado_de_postulacion_candidato_postulacion;
       cargos          hzndkfkd    false    243    235    4049            �           2606    17287196 #   cargos fk_id_parametro_moneda_cargo    FK CONSTRAINT     �   ALTER TABLE ONLY cargos.cargos
    ADD CONSTRAINT fk_id_parametro_moneda_cargo FOREIGN KEY (id_parametro_moneda) REFERENCES public.parametros(id) NOT VALID;
 M   ALTER TABLE ONLY cargos.cargos DROP CONSTRAINT fk_id_parametro_moneda_cargo;
       cargos          hzndkfkd    false    234    235    4049            �           2606    17287201 (   cargos fk_id_usuario_administrador_cargo    FK CONSTRAINT     �   ALTER TABLE ONLY cargos.cargos
    ADD CONSTRAINT fk_id_usuario_administrador_cargo FOREIGN KEY (id_usuario_administrador) REFERENCES usuarios.usuarios_administradores(id) NOT VALID;
 R   ALTER TABLE ONLY cargos.cargos DROP CONSTRAINT fk_id_usuario_administrador_cargo;
       cargos          hzndkfkd    false    241    4069    234            
           2606    17795560 1   postulaciones fk_id_usuario_candidato_postulacion    FK CONSTRAINT     �   ALTER TABLE ONLY cargos.postulaciones
    ADD CONSTRAINT fk_id_usuario_candidato_postulacion FOREIGN KEY (id_usuario_candidato) REFERENCES usuarios.usuarios_candidatos(id) NOT VALID;
 [   ALTER TABLE ONLY cargos.postulaciones DROP CONSTRAINT fk_id_usuario_candidato_postulacion;
       cargos          hzndkfkd    false    4073    242    243            �           2606    17287206    parametros fk_id_tipo_parametro    FK CONSTRAINT     �   ALTER TABLE ONLY public.parametros
    ADD CONSTRAINT fk_id_tipo_parametro FOREIGN KEY (id_tipo_parametro) REFERENCES public.tipos_parametros(id) NOT VALID;
 I   ALTER TABLE ONLY public.parametros DROP CONSTRAINT fk_id_tipo_parametro;
       public          hzndkfkd    false    235    236    4051            �           2606    17287211 8   respuestas_candidatos fk_id_pregunta_respuesta_candidato    FK CONSTRAINT     �   ALTER TABLE ONLY respuestas.respuestas_candidatos
    ADD CONSTRAINT fk_id_pregunta_respuesta_candidato FOREIGN KEY (id_pregunta) REFERENCES assessments.preguntas(id) NOT VALID;
 f   ALTER TABLE ONLY respuestas.respuestas_candidatos DROP CONSTRAINT fk_id_pregunta_respuesta_candidato;
    
   respuestas          hzndkfkd    false    238    4045    233            �           2606    17287216 F   evaluaciones_respuestas fk_id_respuesta_candidato_evaluacion_respuesta    FK CONSTRAINT     �   ALTER TABLE ONLY respuestas.evaluaciones_respuestas
    ADD CONSTRAINT fk_id_respuesta_candidato_evaluacion_respuesta FOREIGN KEY (id_respuesta_candidato) REFERENCES respuestas.respuestas_candidatos(id) NOT VALID;
 t   ALTER TABLE ONLY respuestas.evaluaciones_respuestas DROP CONSTRAINT fk_id_respuesta_candidato_evaluacion_respuesta;
    
   respuestas          hzndkfkd    false    237    4059    238            �           2606    17287221 A   respuestas_candidatos fk_id_usuario_candidato_respuesta_candidato    FK CONSTRAINT     �   ALTER TABLE ONLY respuestas.respuestas_candidatos
    ADD CONSTRAINT fk_id_usuario_candidato_respuesta_candidato FOREIGN KEY (id_usuario_candidato) REFERENCES usuarios.usuarios_candidatos(id) NOT VALID;
 o   ALTER TABLE ONLY respuestas.respuestas_candidatos DROP CONSTRAINT fk_id_usuario_candidato_respuesta_candidato;
    
   respuestas          hzndkfkd    false    4073    238    242                       2606    17287226 A   usuarios_candidatos fk_id_parametro_anos_de_experiencia_candidato    FK CONSTRAINT     �   ALTER TABLE ONLY usuarios.usuarios_candidatos
    ADD CONSTRAINT fk_id_parametro_anos_de_experiencia_candidato FOREIGN KEY (id_parametro_anos_de_experiencia) REFERENCES public.parametros(id) NOT VALID;
 m   ALTER TABLE ONLY usuarios.usuarios_candidatos DROP CONSTRAINT fk_id_parametro_anos_de_experiencia_candidato;
       usuarios          hzndkfkd    false    242    4049    235                       2606    17287231 =   usuarios_administradores fk_id_parametro_genero_administrador    FK CONSTRAINT     �   ALTER TABLE ONLY usuarios.usuarios_administradores
    ADD CONSTRAINT fk_id_parametro_genero_administrador FOREIGN KEY (id_parametro_genero) REFERENCES public.parametros(id) NOT VALID;
 i   ALTER TABLE ONLY usuarios.usuarios_administradores DROP CONSTRAINT fk_id_parametro_genero_administrador;
       usuarios          hzndkfkd    false    235    241    4049                       2606    17287236 4   usuarios_candidatos fk_id_parametro_genero_candidato    FK CONSTRAINT     �   ALTER TABLE ONLY usuarios.usuarios_candidatos
    ADD CONSTRAINT fk_id_parametro_genero_candidato FOREIGN KEY (id_parametro_genero) REFERENCES public.parametros(id) NOT VALID;
 `   ALTER TABLE ONLY usuarios.usuarios_candidatos DROP CONSTRAINT fk_id_parametro_genero_candidato;
       usuarios          hzndkfkd    false    4049    235    242                       2606    17396389 5   usuarios_candidatos fk_id_parametro_nivel_de_estudios    FK CONSTRAINT     �   ALTER TABLE ONLY usuarios.usuarios_candidatos
    ADD CONSTRAINT fk_id_parametro_nivel_de_estudios FOREIGN KEY (id_parametro_nivel_de_estudios) REFERENCES public.parametros(id) NOT VALID;
 a   ALTER TABLE ONLY usuarios.usuarios_candidatos DROP CONSTRAINT fk_id_parametro_nivel_de_estudios;
       usuarios          hzndkfkd    false    242    235    4049                       2606    17287241 (   usuarios_candidatos fk_id_parametro_pais    FK CONSTRAINT     �   ALTER TABLE ONLY usuarios.usuarios_candidatos
    ADD CONSTRAINT fk_id_parametro_pais FOREIGN KEY (id_parametro_pais) REFERENCES public.parametros(id) NOT VALID;
 T   ALTER TABLE ONLY usuarios.usuarios_candidatos DROP CONSTRAINT fk_id_parametro_pais;
       usuarios          hzndkfkd    false    4049    242    235                       2606    17287246 -   usuarios_administradores fk_id_parametro_pais    FK CONSTRAINT     �   ALTER TABLE ONLY usuarios.usuarios_administradores
    ADD CONSTRAINT fk_id_parametro_pais FOREIGN KEY (id_parametro_pais) REFERENCES public.parametros(id) NOT VALID;
 Y   ALTER TABLE ONLY usuarios.usuarios_administradores DROP CONSTRAINT fk_id_parametro_pais;
       usuarios          hzndkfkd    false    235    241    4049            �           2606    17287251 <   tokens_de_acceso_administradores fk_id_usuario_administrador    FK CONSTRAINT     �   ALTER TABLE ONLY usuarios.tokens_de_acceso_administradores
    ADD CONSTRAINT fk_id_usuario_administrador FOREIGN KEY (id_usuario_administrador) REFERENCES usuarios.usuarios_administradores(id);
 h   ALTER TABLE ONLY usuarios.tokens_de_acceso_administradores DROP CONSTRAINT fk_id_usuario_administrador;
       usuarios          hzndkfkd    false    4069    239    241                        2606    17287256 3   tokens_de_acceso_candidatos fk_id_usuario_candidato    FK CONSTRAINT     �   ALTER TABLE ONLY usuarios.tokens_de_acceso_candidatos
    ADD CONSTRAINT fk_id_usuario_candidato FOREIGN KEY (id_usuario_candidato) REFERENCES usuarios.usuarios_candidatos(id) NOT VALID;
 _   ALTER TABLE ONLY usuarios.tokens_de_acceso_candidatos DROP CONSTRAINT fk_id_usuario_candidato;
       usuarios          hzndkfkd    false    4073    242    240            �   e  x���K�7��]����E�v�E���r�P5蠧{Џ�On� 7�\,����ؽ�X䧟�~v�b+R��*�8,PN�D��}���i��E/�'=^w?�e7v-䎵�"$������k�V\��
8�}Z}\=-�"�0I+\C�q$�X�P���cUWD�>��G�:w���7�2oOz>� R�}^�_�[\�x��P!p!RW2-���bj-�_^�p����Qt��ӳ��}�=�S��������_��J�z~��<����v:n�49?���z��l���A�[�����'�'�r �4��DZ.�\�8��JD��$��CƘbD��y��7T�}�oG����p�U4@
�PB��y)�H�§���l�y��Ô����&���X}�)E�����4���r�&߻�O�o��ic-�+cZ/����J�}�X���`���]�����E���;�u�|��3��u�˼���� ����k�K�>&��p�����5�hu ��iHHz/͛ �t:w�����c�owc#���b�:Y�,x8��[jud-���f&�V��c�l�ԇ�--.T�L�j+���ѱ|Ed�~���]Ӷ�5m4��%6Ȧ��L��h̭+��rOS6S��&Z�>��s�P[�аI�h8Y���r�:J��i�v8��mz�Qd��ɞ�ّ�'@��Y�����v�ܚ��y)�l.I�f[!tn�����D)}Tי�Z�?�ݮ{KS�̋n~y��D�=�uUH�h,=���%���3����[n��F�d�%�T¨Q�:(e�`��3/iљi-pl�{.}:���^v[sR�ZܢF����T��ҺS���74Ep	TR���e��� ����      �   �  x�m�Kr1����(I�z��fb��lz4Rx�8N�}��"��E��Sս���ۓ�0pQ+���ܢ䤜Q�����%�F��� �=VC��K>>O>���e���u�]��vk�L��L	\8.�Jb�ty����45�[B;�A'�9W�o@b����(Rh���c�)L��v]B�������n0kG�f�q���}[��K��ehl���M��<�M���j��t��Nux|�( [�׽��ҎV��}�i>~����&����A
���S�+�]� to@[˕�ȱ6�	S IZ����R����祯X�=�mpf�ã�e�Z���\�đb2����2͛�R�m�Fn(��G�9)z�5Z��@j�;/tͨ\T����?^_/������v1�l�z�i�G���-@vP;����ɲ�7�+��      �   5  x��VK�7\�N�|$?�� 0�O���E6�?C�F=�4q�m��� Y���R�1�텶���z�WU�ι��Q�Z���1z�5�DW~h�y{[6�����n�m�~?�m���h��2����R�w��������x����2_�l�+9|3nj�7}S0���t|��/^�]�/�NXw��M��߀��x��O3��p�r����Z*���^����i��G|��r�����-�{{z��k�a��`��JG�y4�&�vvbb��P���sTU�U.���nV�HBv�#�4']�K*Tߕ�U2��0�H2�{7\a���ve##�݁���m�2�O��Q�5��M�1d_VJc_R�M5B'�OVE�Z��;�f��=����nx�����A��ቍ'6�A�'O)T:7�r0*���\�-D�?��3��/5s�O'�8�v<�dm��3����a�D�^T���6�̚b?W�1��=~�Ϻgר�������{�Pw>�]D���Jړ��	��{�|^���M���X�m��N����2l2Fz�I�=�W1y�6�w6�P>ö�S4�k��MP�x!2�|*v����"�绘�bN��o>���נ�'�.�v�V�KVN�8��Fvp�zo��p�M]�/��Z�	�E��"pgZ7.;�5����\Ӊ��lN���P_�T�]O�"S�7&�JTc����|�($>��g��}M�ͼ�v,��YƏ�O��ٴ�<y(�AZ��X�H�*G����*�w-�\BL�RbOY��`5(	�Ȳ�R�h��z��#��l����M)���2t���n����hV`�F:璭4K҇7���ȿWm��t��y�|\;��lͅ�w܋f�/�!(��(i�q�J�Ó���)���������|	�{E�)��[`w���eC������4(˴�"
C5G��P{h ����a������}��"�lv2>n/�}�G�ΖO��6\*{��Va����e �T��-79%3<ؽ�{������q>�a���:O�mz�I���d���� R�o�ªA���l`�a9���jZd���ߞ�o�?� .�#q`������m��|J�Q�%r�n֗ڒ�,+Oљ���l�ĩ	��\"8�@x܇�����<���^�nn�sh�NCrk�&․|�Q:w�׵{��FC�%�e�+vU�\�I㡊j��Lm�>WBtI:����v����矴�v$��q���8bM�$l�Fuq�p(!�H�v��`�NW�Y($Oj����N�O|MZ�T)5��=��飫W����tx���}`^�y9N^�<�иb�R�.�k�nѓ�!q����i�Z�Ǭ3      �   X  x��VK��6[ۧ�Ȩ�T�g�F��!t����0t[�X,�e�y��{S�#G�ѢF�]��$>c��1�F+�<JL���zW����f/�YKR�B�:�3�_�-����c��|������ue�i8�o�� 4g=�mt=�gXt��:�����EJ�-�j|��`���~�'��{���'��؋Փe�u���M��X�gXz��	�8MJ�D�R�F�4~�E?��*��{�/?|�H�Yvv	J+��0��^��ݒ��[��V��x��)���?�����jzG�A���[hO�6Ż�G�?���3"�h���Y�����=�_X����������FW�Ӕ�j�.^Fu/����x�浖[o�
I/k7�`*J:����:gTuF�eZ��T�'AJZ�,��K���Q<�[��g�=ѣU�8gep�`��a�t_����f�3�Rãs��N�ׇ�����yr������F5@(3�n2��a�k,;:����w�sh����K<d"vk�f�,;���9R]�}_�3��)�I���{�Y��T��3/��$#}��.�����9R
Z�N���d�%��v,"ݠ�
@��u�Å�"�x�q�dP�W����RK�P�F���}\�,�L{�]M���ȇ�Ծc�/6�Nz5!^$��qV�٩����Td�֖��}��m���0`A�XT	^:�,6���-�`6X��x��h���u���&mȅB!u��b������5�Y�|���<NizV;��74ꔽ 㼆à��H�vt�>2�;��ʅ�c�$ʾ1?*U�6A�h��'F�N��ׅ�u�e���lfo@G��6R!���!Otv`��<0F���c߱īA����-����^6}e9�7�3���\.cV�-������x�=U4퓷Gqm~5���p����F�F}c�9�n-m��
9"~�P�tm]=F\�b�\V�b/�%�u��x��\�-�I}\�������Q��q@��.%�� ����
0�8��Ę�1M%�����?�no�t
~Y��$�mg�s��wn�q���>^����(rq���?# _�8���s���Q!�      �     x���KncU�������z��g-�!���<��A�8rl�%�1ʑ���Ȋ#��U����:��S:h�
�]���Yz��e�̇��ٺb��,7P�j^L�N��۶6F�\N��fgI�h6����U2�+kCY��-w��C�l?�����H�9�UhC
PM)�>��	��vf<P�4��"�L�xL�ӡw�@�ض��o���^�c��������εOVA9�vh����T��)������g�G��=��^`N���j�����ܾ������Y�ȑU��/�Ҡg�!Y�G�^���q�l�����?q0���u&=���}��Fi��M\RU/���:�g�N�nH�h��1oKX�
i�X��0���lfbE�=��4��Ho
*�����w,�K�>�=���eS��kh,4F,�t�U����'�#�Ӊ)T;�%e�i/y�Z]�Ub�>�iE�>j8źo?�˳χ��<�s�Tw����9�p��n
�ob��a&J������w��տo3�0��i��!�B� ���jm�}	�<���ӝ�rF>Bt�s*x�ϱ�9nCb��:h{y��t���c,�e������O�={��#�ܼ"�F}�n3�Z�Na��b8�,�S�clO�ӷ��k��r?����-Q*�D��zɣ�g,(�%e��"t#��?�e��G�x-���qX�1��)R�R����o��vz|8����PA��ȜJ�[���0a�Aĩ:m�_^ۼ��ޞ�e�Ia]ቛs���!�FZ)O���s�1Rq�6I��{�>��
�<�X�mG oMq,���㳿��xhw#E�jJ1�p��Q�ڌ#[[�ic2�UW~'^#���w:�8�n�^f���M" ��� ���l$C�A%��8��B1�<��vh�$�!3E���}:]^��e�ryjwR��RP����*�0Z'�TTw��O�BLO���|^��a�����ˑ��tj��ǜ�f�$ʙ��+k�vӤk�$\[[�Q�q8�K[�����K�ڼ�g�Y���/Ǿ�ގC�      �   o  x���M�#���U��D!#3�'�l/��aX�Yh�g��M6�l	�mta.�W=���h!6�&�EF��^�\K��R�#����Z)�Gp1����i�o��7ڞ_^G��v{�Ǉ�X{��7��L�O�m� L�j%+���u$v�\��\!��w'	'�;{�ȚG+쩏�I�l��v��RBa��˥>�'۞�6�>�x{h��o�m\oc{��������m/ܮ��2P���]�x]jk��9�q�4�j�O����}�W-��'�ONw�ACZk��Y*�Us�ʣQ�е������x�_���Wo��N�w|�~�!>��S	c~��N���\��_��X��~�x-%�����i�Vqxk>��j1~&7�F��k���ʃ��P�[Ƙ�6�,:juf�%�������'O��:��AũP6����1�;U_6�S('���iY�ܔ3�j�I�D:ӤTdZ(��ܗ�\���m�ۃm��`�m�L�G�<�����H5�H=��-s�AW�6�'q';k��	st��44��Q��q�5u�$��Ŀ�����>)��`�(^�'��2-�PVa���1j>Eٳ��Q�!5[
d�b�=R�ƀy��⫾���:��ݑc<E�k���*SBB��nT?p�V*��F�<[r�OP�'�NU8��:�|�ȔjF�!E�1ON�ro��[�UW�߫�*>�j���M�G��4-d���<{k����5y��ջX�h��-�	�?�d��uXfe�M����8w��c�uj7*�
~Bj�wu�-+_+��\	u;]�ʌ	���>���F��`�4߾ �R�8��c����H�(�(��Y�Ё;�`6�˛�B��A�q�7����h��)�6�^��?t�]�x�bԝ��gRn�\�=C	ls��2/'�vf���EoJv8��a�;� �y�寨��q\��h/�g�6A�	 ��/����7�S0<��z/�	|��E5�嚥�4|A2p��B��]�t_��� �6�e&`�vlO�,�M�?�����A���qq#��؊E�FN��9�x��C�z���]�eeda.�MD��T�	u	����/�%����p�
���	�C>�D�:G�{�t� p�ǂPS �Wg"sǨf5�b.o4���-�<���>��[.�Xr�%����Z�g,E�-��|��gG�DN�������'�z���H 
�9��N��b�.��!"�C���+��R>շ;�?E������`
����Hc�W�W`�׸>�b�Gۥ~7�޸�9��Ì�ZX�h ��A���G�V�/���u\��BڽF��*�z�c�FYb���[�x�׼��|{����v��ÇK�!�
h��. 4�CA�+�6	^���D�'�
������� %%�      �   �  x��V9�G�g^��Dw}���
�r��^A�l K����)�
F@�Hh=�NW֑�U�f�8�u��I�2�\�B�jE�rVo��壍˭�K���᪦�D�p%��Tbg�%p�e.䉝ώ�!�#�QtK!�D��n�[t4�9�]��B��jZ�,ﯧ�ӹ>��7x>��R�������ą��	Oq�Jr��q&���Z�k��ð������X Վ��D�$v�sv�Le�!��-/G�G��La-=3wn(,$'�WWb�T8R�-׻:��I�(�N�Y�'�ND��Z��Us�6��-?_��^Nv~��dq><���g��fM�srs���\F2.ǘF�@�˯/�W�}gC߾��O��JY�M����I͵�Ս��HSF����]o���Wl-G��(�j��$2��(��)8DC=F��r�:�D8��8	�Fޮ5n�/-�=���0���.��d���êF.φ*�e��T��i�|_��c]|0��8 㤨�rq�k�L�8�;� ��v�ߠ�d����E��@�-�G�,gJ��}C[������y�ڊ4�w<���rs9U�|������԰y)Q�A:�L\̊��6r��m����w^��˃`	xk�*+I$�V\�=�4\�4k#a��</��n/��/�F�Too����D�z�Q��J�C�p.I�a�>!B�b�Ҭmy}���<�z]F�zirGo���'u��V�G��DygЖ%��+��ds
{@w���f�(Z;����a4��D��Lл��ǻ�u%�ݕ0,B��������>�Ud�k$�����(��KO����nO�ߣpB[R�U.m�T��6l�Wr����O	��X�K���N� �*�����p�IF}f��]ki��Ö������ۿ[�2>���G 'e��;]���;����e.�?t-ڡ�"�.A&k�{,�u��0F��G�z&L���bq>��՞�xã�R��-G��="��]����/��r�v�s?�q��_Ο?����H��&%X��(������E��nn�X���۵�zp(�L�p�4����`Nu�~��*�*�B<�WJ�GJ[f�W�q�e��A���p-��t�~-��&=���Y͚��ݭ!z�m�%�-�<�1�Pw@M�E��p���"M���$8H`�c��Y�=,��3+��bc��1I�a�c[��o۬`      �      x��\Ɏǵ]w}E~ ���B���ǝ71����lgV�n}���B�� ���s3��\�l6�TwUdd�����5��f�IŴ��%�$3�y�C2����u�f��LmYh�1�u��'^\����~v�_����������q���8�Z�}_�a�n��aw����S��OG|�Ǯ����J��8�݀_��i�q�q�vݫ�W���7<�/��Nק:�ء;�7}��C_D���ݾ?�����Ƙ���������⛼��2 ���4�!��4,�>��c\��D����BH~�.�F�b0���Ǌ�bu:z�u(��O�{�c�9��x��i�3N�����D�4�p��/�Br8�餸��ۭ��)R�,|b9�tp�E#��	����s���_�ER�þ���p���솫1�d�L�]�H����z\�}j�<;�>��x��:Ņߤ�&��V]�v>`2x��M
e��>��i����b�ҡ��a��������Ĭ��@�(���V��s���"O��G���[�a�R�m�^y���`|C��i�h�?9Ϭ1�ۤ��_��P���J�ߘ��Ă��R�b>�PK�U�8�W�X�Pz{<1� e�K���+�V��|f%W�U�ʂN��d����ή��Su��1��_N��4��z�N�!?�~�C�	 ���8�c2������e	vi�p�R��!��4L'aYR�����%�Z;ױ~Wg� {�>�	�΁��@v�JQ[&B������W���wi~���xv�1k��Tz+��6lT�"#���}A�ͶZ[�5�t�]�ޔļ�p(�-�9%fA:���'.~^�<�~��q��:���/ ��$:���
������=�CE��R��R�j��FiW Ti��� �`-T�V�"T--˚��iR�H.��R�������t�MG�Id-W�>�q�k�Ow�����������ݗE$���X��EfǠ=(�
�%�!%tm.���qֆ�s-Q[˕�~�}��d�� 3�B����#�p�y��]�Ex:|�z�+�%��~GԸթ��vg��h��X/f�y��n4���3�^ ?eH��T�"eIU�sS�/vT�R|=t9U����$t=3��b!|�o�%����~M�O
J�z���sU[1���g+�Ta��V!x�)&[]f)$ML �ڳ2jB�Q�s]���p�uק��A�
��~QȾ�P�� 5"���r�O@4��V9o��X�db%F�
^X%��薴-����lʜs�Z��⚳dRc��l�V;I�K�db]7ݛ���ϼ�Y32���n���d��Ƌ��y�S���F���ZB^J����7ՙ�9 B4.b� ��Zb�8Y
�ڟ�R���a��̜V%d�kb�E��.R����.�0�� �`lCz]��W?t��g���N˦U���s��CT�@�9���4�����rB6:�o��u�m0B{��|�_L4��9CrH�Y�2�ۖ~A3��?!Ӂ�������x���~�$�z��k�����@��Y[�CE�(�`��n�fc�5��x��J��\��֗�o��!�M�`Nf�D>q��������d�c +b�����\}�8�p�⼑�/�d�����J)`q���ӮE���S��"�eK�N/fC�}:��D����-�9�g���?u�.�G�43y  Q�`�?�;��Fe�����~�Lo��P�s�L8�~�0���-7Nh��r�Rk*	��(�k��*���9�t�/K˩9m����G�h?ę�����������歟�C��~�o"E������i؝(\�M�J1z�$?ː��Ry��PZr�QMhe�e�&�tB`�]�v��r�Ĺu�g�e���̭��4��H
���ӲaO_�BnjFV�~5�yI�ܐ�����Vf�fV��Z.R���?Q��dT�"b���V��P�j���P������T���d�:���8�Yj ��HE	|>����A�Ȱ�n�OE�'pNd@���zk65TSekL)[Pfb ���XCiY�!R��l$EvT���}�}���iAgm����E�n���[����|+���l���H�Y	�%�X'�3kʨ����z<o|� ��E�7��6!��I�^)o�������N�n�ɇ���ﾊP�����ﾺB� )��Υ��j1$Ӟ>��|�!D"�������PfC�����?������߁�Tv�����%��T� m,rc���A�S�@��:�j�|�T�x��M���c͇a7\�~�Zdw�W�j�ߛ�0o���Լ��@��PO�r�6�|^�M��h]A�+TֳPKdY�P�j^w��}�d-U��y1��R���#G����n�]�L��S��Pˮͻ�wL��hL�)��k.U�j%��ߪJ"2��>nĂB�TI5-5\ي�k<���_Q�o��tWP�N�2���ȋ�&h{罇�"0X����u�ii�~pW���?c��ݥ�[m�@3�lM`Bcj���i�46z�E=�	Wz	O��3�$����ם��m����a\�5�����L�z��2l]0Nm�(�a~VxnL��Y�\�L��0'~���&�t^v}נ�vI�=�}d�����RI���a�M\��������,���>-.��b�fcDU�i�0cb�)μ�	�k�Z�,�����B,�w0�BM+���v���6��H�p��Om�����i�
��I��"{I˸-x�3xDa��䦤�ʗ�}��9�(�B^Y�x��R�\� ���O�~�x��Q�7@L�݅Xnؽ��N}�O�;�.���
Nz�����)��̘��-�4.餢�(-d#c`U�Fg�E�
jM, �M9����w�9j6
:��~~'����5��@�� q4�y�����C����ZN�,�#０rMqܔ .�� SU1hP����9���?�H����Ċ�K��)��d�Cn��a�k��ZL``�,9٘i�;'��.��_->J���$�����yX��0�;�˵��md��֪�r� 	,b�Z9圊qu��Ǵ<RJ��V&� L�D���;-a�(�	y�.��p>rV[A�R�T�fE+�sV���+��N�c7���z24'���|�un���=R�"�������o?;c�e_�� �mK���iͿ���hx�al\�7a�c���Z$�)�ejX�7pK\� ��˹�s9��&����ʷt�P�/�=:�{�3�#e���!�X����.~1���Íy�K��Շ�yV[����t��e:�?�#� +�Ҵ���41��#۸�_���u�B��������B�{ٚ"D����E6w,��sj�z�^��xz��N�sz�z��x$<, ^�Ɯj��#�֗wΎ�g8�v�?�=��
* ��V	��D����32���!i�?v���R�h�$�f�(��Ȃv9H��o��w�~M�o���ꜙ��ƫx���)�ku��Տ����������0N36����luw�K%Qt��C���j�����>߭]����3��u烵�Y����n����"�u=���f�՛;��ݻr=���"�v�_>R������j�������7s�=n�z����]��/㈉�$�J���0�tt�����U�\�,�� �+�V���$�@��/�ލo��?�7O�J�K���iR�@��X� �5�P�X�(ͺ�/ �G�^"�tkX�- ��D(RI����R�Q�G�D�9�Jh<��n�x�_�v��!�T_��7�)�Հ��a���oF�̶[�/ݼ��3-­�t�B��#��9*w�ыW�W<�dNW��vC��W��k��[��N�C��~A�(T�$2 _G[X��؃����"�<Qn�d���Ibǆ�c3(2A8�fY�\�$P>�W	��}�#�k� ��|�mОfB����(v�q�9v~m����R���Ģ:j��"�#�4^k�D�3���]T��BKH���¯,�V�06TdhZ]�bi���J
׸k��D�i���ef��|�!}H�;��tv,hq�^tjZ��.��ٻ�� �  A�ȅ�8��F9�}����'���+u����=�t�%��^9O7�z}�|� �<zX��W|������}�����,�cݼ�czo��r��� �Q'ɷ*�E�4!�!�� �T�c~h���w�ɚ��k������hS�	����l��(֬C�*(p���Kp�5�F�#�S�@บ���m���nb�E�&�T(S(t��'@l&i�oMU�ǒSE�0 S�[�|�x{����F܏dy����|�o�>��$.��r�f����N�Ge���]�\\����鶀9@=�* ��\�{�_g�? ��ᷯ~�ӿ�l�pB<��G]������-�B|tL����uR��~y�;M�K�����~��[(}�x�o��0K�bQ�G�r]�X���sp?Z�Q9�)����p��)��3T����}1�eK
\���hk�S��}n��`L��G1x�K������B9���O��f��o���      �   �  x��Z�r#Ǖ]�������fD���#):D�Co��.�@�ҧ̮�^��᝗��d A�="�E�H� �y��眛�/�"m`D��s2��i�&��bl>�~��ئ���m�껔�~��bh>�/r��qھ�֛��������b�-s�|�8�?��6��D�I�E�p��9������Tl^�Eג��~��7^�/�6��4��bۧ�݌>���j]�i����z5�k�y�o���y\�ŀO~34���\'�%�K� J!�fAư Y�w*��Bấ|N�\�a��\�D�
"Y�D$ǡ�DG�>0�23���b� ]es���8��1�!@|5��/��j��+gJS�,�TA��8#�" 3)3'�eK�RQh����y>��o	����3-�sn��UԴ���iˊ�ԑ�y&�gI�4(���D��w�)��'�Vؔ�1K�f;��"��H�ԧ�"c F����H�|1 �_5nvN��r���VdA�B�D'��9��}�N**��GtH��O�V��A��;m,	�2W � ��\K���\�A���5#ȡ���G0��u�u�X� H����@�6��h���7C�xqlR�#�?��bX\dӜ�fg���?}�7���\����W��n�����Vg8����Q8��cO��^����)����ؕ���e����Y^��N^�]%?�N���f���U{��s>��bH���IK������J�
��dX�e�u}镯��lQ��,{��� ��9��eb=UT3�"e�_'�"&������9�sef�K��~ R����D0�������S���<�7;��/��=�ݙO�;b&���ُ�j����1��qFBҖ8%�Y`�~
^LS0Er����؁��K�ό�b{\p=��("i� >d��:.Q��UN��k��3���ϕ�s6�0����X�U8_FeH���tQΩ£8Ƽ�}��<���1W�����nZJ�R͙�)ܓ�.O�⌋����DG�%>�L4R����N輹��C�s6�A6cĆȁ .h3���Y�[�0s����=Ct����x\���Ϛh�P��[bYLDӚ1*��!��n��}���1ɕ��O��p�r&�3I�&�\�cN���n�hlJ"u(�s���!9e��Y��D]O��]�z.�c�6f* �S�4Ì���2JȀ��+���Ǽ_���>�?H:�L�������**vY�5�ɰ!�������PjS���n3L��z���9�����]n���ت����?����7&�|9o?�muݺ���z������;X�|�,�~���?:��\#'r���g���p���u_��������VG�>;ݞ]M'�����b��m��>��6S���]��§j�P<�$��Z\I��B��p�Q�W���suT//��JY��M���a¸y ȟ~v�J` b�d��T+��0����=|��Vy�Eqw�����n���U��OW�9�ȣ�������"�� 'GŝL�{A�@�pl�i)x#����,1IJ��BZCu��d���p������z|@3ѽ9r�?����v��78��y��ds��[�h#���ݢK������N�nW~��_����}������K��w��� kT���h��߮�{��d���I<2�����c|]#��C�.�y�׌�0����i=�$���{�8;]tgh̆���������o��G|��nw�)�G�KzDu�3\�fӗu�
M������h]��%�x�CK-�&��M�����Z��Բ��qQ�Ca��&���o���sNtqu��AaF��ȊB#�Bo%�p��}���ӫ�Oj�כ#�>��H:�w�}�����X������ud~����:{5b����� �
�z@�V���	�J
���5n�J0�ޒ�3ȇgG,+3	�PFa��l9�h��3ZW0���[8�o����lL��>.�%l���Kȑ)�J�͎
o�!?��G:�=�����-�J}LW�gz�5� Se���I��*.E�_Nh<� �� �hI�!j#R��A��Ű�~{�~1��o�w�?}�\���\7���a9�w¹I���>��u_��Ć�|�|���%L������
����������x�Oﰯ�{/F��S�w-
�~m.��x7�~��^t�������k�;�EL�o5f}��~��U��!����c�ŉ7w+[;�F��N�w���K�q{�w�m; �Ͷ��_�Y���z�
�t]oX_N�f���6~1���<��v��f���np�D��4"�M�q������Ƿ�1��r���݀�������aR���_;�ZC���W��j��ث��g��F�f��>M�b�� 9��]�U��r�A�z�^�F�/�
�����)Kv�:\\�����V���b�m~/$m��8@�~Q��� �.��9�����y�[z��޿@z?1�������i^��t��֌�$��4�shϟ��$.�R#%FI�B#8	p�$Nc1[������2��C�@�Ǵ��-ku}�MJJzc�\#���`M��%c�<��gK�W�X-�Ć �p\��%vǞS�r>Wl.ٌj˔i����Ԟx���H�׸��8�q�kU@���/r������ߢ!��ƱSD�a�?z��^��C���8��qJT`\Ka��᱉��ĶL��1��$�j��JsH:{@�X�H�C� ��I��L�b�j��`��}޳_�f�I}��4+���%
��V6�E�'u��k)_�;��a��}_�H�Kץ8��լ�n(Ĉ�L�+��R�5u�u�#���6$�(c(h^���.G����+��Yi�V�kܮ*��a<1����E:$m�eG�s���QB[l���A�:V�#z�<�YH�G��g�+���O����a��r�Y��02ԅ��!/���c�L�j��?*�"-��JP����u�i�q��8��v�ҳ�E�N�	�ܫA��E ���H{��@6Z�,Cc�l��UڊH�s`o0�,t�<Р�ݹ�����g�3y��$��r"d4D����W�2А����h
A����x��GN�&/��z���~��C�]	�3��.xwu]���v]n��!j4��f �rr�C*ʥ�M��b}Q(�0�T4	�B�WHdw��ҹ�V=����M�kݲ��P�*o���x�2)QOr����K�����1뛗E����^����ے�Y���E���l���bU��w��}�b5M�6hP-I.��g2	�hS	49CM1�wԈ�8�ѠX	P-�9�p�
��1{*���� zN�L	ikD�
�g�����Yv�r����	ja�,I I��ͫ?�Q��jLy�D���I���曃d���%�0�l4��O�d��@xA)L���y�#QT���I���i����X��B�jQRY��S묩�5y�����e5�'�����b+�      �   �  x��Z�n#G�]��"�u�6�������zO9�)g��.���^�b��l�؜�IJ$U*Q�j� B�DFF����Hь�BD�mLg.��B0�t�҄�Zy댮հ$t`�yμn�)ύʆ��*E�J�Ք2Ӷ5tvL�d��9)WM�d���L�\`�p�|i���kn�M�*�¤6�i�*"Z�eT)�ʪ��b�3�:aod�1b��&��Z��m���Sw?��nߍu���i׫���a_o��Ԯ~��}�M|Z��7�~�����M��N�]���wS���a�7�~�~�c�����}}�������5,��vC�)���ż����Kw_'��,��݀e�t�m�r����P��mw?w���v�9$�Oݐ�:~��a[������;��w)TƱf����v��ex�/�,�V�vW7�m���]w$XKM�۾��G�Y���%��sw�����Hb`���?h�6�wUǺ�O�BZBF�ջ��q���oq��]�yaė�P�.�����n��������Ż~��<����|�t">:�s��=��� �J�4����Sw�������((�>z]��>��CK��f�|7z_�KPvs0ʉ(����Xo��]|.�`|�O��<|q�wQ)�Ҳ��ܲ�Lc"5.l䶕���;ٜfQ�ʴ����32�Xcp�5B�l���b�ZKZf�w��[���U2���F��X��3���..F��<0.;)o���b��¬�����0�PA!�o�ݸ����_Ys\�W�u����������9@Կ�	i~�Cڨ"������O�+h`��NtZy�X�|@F��Xj�,��,~<kW�����v�A����8������[���((�Cx�������c�s��3,##{�O������h6d3B>�z��}��ͮ��.���p�e�;2��͹�^��g�=A�lm \�TRr8B���E�zS ������c�r3X�WK՜H�3=w�k�YvH�g��o� �Bbz�U��V/�+n6>��_��:w�9��`�pq�RW/��<���\�.��Ti�����>���P��@���(�ߛ33D6K~���3��唱~�q�f�cs�~��m�B�X3���Y����/���N)J'<�U��U����:H]��M]W=|M�f/�"z�y,5e�I<��+��)�D��.��(��L�����|yk������F��[��!��cK6O�#��*�χ߶Hx�$��CP�[������g��IDn����g�ģwqK���R����r�q�T��l��3�TZ�Ȧ�� �~x��@���dK��0���/ò67>�8G>v�zX1�����t�E�u�������E@-Οp�#an%Y��v3��9!�'#g`4U;xy|ĺ��<��C��/��L��.�,�\P��&�yOUo1~�EK��F Ac �Ws�
�Z���U���,ѝf�b��NEeDki���Eʉ5�V�XQ@�+:f���I�2oɆS��;��6(����n^��<�Zk�!p�*�lV舵���b�Yl-%D4�֢��jV����H�*/Mչ0i]1�VǤCK��Y��:Ω��fm�J�ɟ[hP�3�a-�5��!�p2�B�n~P��f�3�5X�$K>V`��F�\!����ߨ��B
{n���>H�4�1�����E	�W1�ă��ZG�Q�^S��lU����?K|!:�o������g�`�R���-,Y%X�Ε���]g�o� ��
�E���:���]Ϩ�����3�^�zOp�#(ڞ0���?+f����� ��f<��L�Q�QLZ?Cp����Y�D�%ю%2��_���|E�����?���3*���@��/�}֏v8����qLA�<��<��=�����A���g�@>�q�fAu��.���U"Q���"k�(ew���v��X[JE�y�o���?�5�ܛ'!���ӈ6iKr0(�,߬����?8هX�ۦb���ɗi��a2a�]���1і�^a���b/��K-ف5�?>���o���s���������z�s��F�G�I���'���ݦ��`ٸ'ٖ�NP�Y?��'0�l
�i���P��2@1|��'Jq��*�)��PǂE<��t�^sղ�3E@w�����5>s^�H ��(T@�DV[�z=���P͘���@4�T�A@ji��8�����j�$�"�O�P�	����`#�=*�����N��Z�Ҹ����Rk�P��Z*�Fk���2A�QB�q���[������4��4���kc�'4��z<��[g�c%x�'9��&�'h7���sR���C�i�l�]���L�:�YT��smX���-���a%6O@�aB����';zb��,c��8�y��Ϗ*q2�q�2rC�
����իs�Y1X`_�pͽ�,���Q�F�g��gJ�Tc��ܲ4	�XM��G�Z(�����44	���!�%�L45����_PRe��߅���X��4'��&��&��4:���N�+J�g4��3L)�L��t�r��%���[����Đ(fOI��ٛ��K+P��z�� �\<}�`z�Y��C�c�-7`��q�z���M�ĝ܋����s����c������_0Í��L.8��IА.8�Y�!��ƣ`��J]�S>��9��>Ŋ�Uz���8R�
dWC�چ�ƽtܴ�&���o9�-��e@�Jᤕ�$d�\� |T�>�R��*93IH�� ��76R�RLK4R�r�P�j�������<������(�WN�����,��a�Jy����J���&*ZXG&�J�p��,��6Z&�kD3,�l�F0�쾡��#Z��5�u�Յ��9�ǹ.pO ��.G��h�U{]��M544�a���/�������)7�%4X�s�^h�<�S�V`��53ȅ�Ց�u˃1H�o��길����^�>���s��(�>;ED���ل�*W�q����[5�ٺ47&�I�s:O�+uI+m|D7�aS�i��r�+�T#��,� 3	�%�����7�����Y�{P�2�t�~�9V�vk.�웯�ګ�o��Ԭ�P<��k����L�{	�|��PR�d6���Ţ4�NH(-#�2�	����l�N÷w�O��Y�P��3�y�-�>���G]�u�)]�u9�T ��Y��%�U#P�z�|+��+�FBMi��h�(ĵ��졹�Asw�P�$!j��,Q� q��zgBVq��̈^�$UE�Of1:�JaPC�+j�֞���h��>h	��{{����ӕӶ_���!�u���QKK=��q��0ztx���ǫͷ���Bz��_��
������o|�F�b�"��a޽tz�[�4��^K�O^0:�Hwm�|¥��Y��;ǥ#>�SΧ֓��i�@��Ƈi Z�{����ᷫ�:ւ�qV�+ot���a(Z#�"�X� �����f��R�	 �A�G��[�o��ǷV�`ܭ=���������%A�T4�&��郱JV�T/EJ8QZި�:�,�U�t1$�W|[� ��-a�m� �7�d=��8���&�\X�Xt� 5L.�^y�y��Xb� T�N]Ք��<��F�4U?�`f�j�DK����E��[��7��)��OE(��B��A4"(G�J`������b%��Eeua ��/TdnA�tKƼ��44�<�(��Q�p^D\�{��� �/{�      �   �  x��W=�#����bBp������[0,h��ऺ��n�=C.,��
ʜ��5W�����l@.��MU�z�:k��Q�'lJU�@Y��
�T�r���r>L�2�H�raA&ias�"[|22��.'��-��	-G���썿SQJwJ�e�B�\��ŋ���Q)6�
��3~��� ��V+wܚr�VQ�,�ZJH�U�FKn:T*r��~0��Ks�q�t����$lY$�E�=��Y�2|�����۲��.��1O4/۠tA+rIF�N()"�(��V5���l��j����>�QL�+�2x{���#��ʩ"��������#o'��y�*�����wJ&�J#������|E��>�*���p������j<�->���h!�ډ�,9��P�����׿<��J=_^Ac��%�\�+����/���\�A�����qBr�H�FV��o__�<����|��C;�����M(S,fɂi�i���~!�00��R�S&�e�D��"�f�e��4~/�]
�X�3���D����Q�ڋ�|Ω��A�ۑ.?�Ϻbm}�(Qi=ƫe
B 5�}9���-�@d�I���%��I³��5��{��z��G��;i��Z]jVZ	i�v��
�.��q�7\���޾�n�-�&�`�e����>��(�-�
�~�S��(��aW+��+����Yg��O�w��L6�4��r��G@���.t��h*�-3�*�UL+���zRT�����2Oe�<~�e�<-��[�&坪B��#���8�@��䩠��z�nXr��� �ֶ+$0F�H��2���D��[*����)cs%�  
��(�F���ڐ�b�C��7�,��ɘ�^M�J]��a,T��:�X�i�Uq�R^j�:_��s'rF��H�`�iF/�y��y�x.���D5#�Q800A�d�/Z~��VABRv9U֕"|d�)e�6�[�j�r�z�����ʣ�~�-pmq��	H<Ƶ5�6F٬���eV��
��+4Z�0��"
M���u�j^F��!:�Di�5Θ����N9ToXד7�,@4���C��ah�I�Vi�c�� �n��a.ҕ$����;k�Cmn�L��x^�{f�-����.U(Jԓ���,-�,Lw��t>�)�?���:U:-�x��i����<n�a*��\�#u7u�g��2>��x��;��w#��n�0�Գ������+�8A�|�qY{����>Oǥ?�b����9?^mq�&�e������5�a=z��dJ(�,y�ߨe��2wV{�N��}�ZÂ��)At�.����ɶ���q�)<���j��?]S|���Y��e<�g��y��m*�\�G�ӊ�!%���*o�U�ŧ�FmH��@�L_�2���
 ��5il|\�����~�8C&Cd`T��<����<g���6�'�oF��M�k/��> �w�?,#=��-.��6�>C���#m���q]
o���bP�J�:D�6@�3�n���N��T���}7?㽯ԫ��>����3��<���<_Y�KV��XےW��W.]#� K��i����|� $.��K�P��G4�D0��$(JP�Yx�pIN.�6�zh�NS�,�i�+o���H�#i+L,d�f��K�O.K��s��
7>M��Do k$�桟�u�pɊ�_ɶv���u� ]���8-� ���n��_z��      �   @  x���K��0@ǰ�l ��'����+]��\!��-���:���h��gV		;ɱs�
D"qTAr=x�]�82�A9��)Ӻ48�`��l^
���yL���X�4�T�Wd4���S�օ%b{�q��Ҍ��8.�	�������2b��� �rp��s�A���al^�L	�rl�� v�םX!��)Qf�6��\/2,�=���ي����seÙ]{E\�@U/\o|�Rٖ(Dp�pMj�^"�A��X�<�y�T�O�x�#��F�^�^��K)�mG0$��Tp�vGr�������M���|Kt������	s�y���ڿ��t���8-�aO"�E%��t����J�z������\{�x�!���`�JZ�K9��?h�(�	���������:��Pe{�8%�j�U5������-�H������aZnU�m���1�)����r�~-��|�6U[��.�j4.y[q��U{�p����ѓ�ׇI���B	�	>j����x0���k[;HCԩ9ܾ�7��</py��r��:�x&���Su�k~�m��WdB3az��T�`_��m� �#?z      �      x���ˎ\�v����	�wּ�Ŏ�*UeX��r0�!�<)$3�L�.mz��<5��1`�X��X�$c��D�P<73.k�5���)�K^m�!��~�[m���j��!�pp��c�w���V��~��[�m�vu�o���p<vw���l�/�_/_6�����n��o���w��/�������������x�tx����N�χ�����������tx��9�O������f�Y���/Ћ��ly�n��9���e��xXߕt��t�;�����/���|���e�y����?��7��O���6/������o��<</�tz:�>=p����x��������?������O>��y��+\��Һ�iN��s���U��n�_m�&�����w{��K��ar����W���3)����X����x�����r��x��������7ϧ�2ݥu�w����_�?�$JI�?<�/_�_ބ�rz|�=������>�YW��z���෧���������t���ҕ�6����i�|�^�������O����7����������G��������c��R���:G���˼�q7�1��1��1���
uv9��vNwi
s���j���cu+�ح��)�ys���e��/?2���z8�o��,�}y��Ȗ��i�������Vj����P�����_^v�_�i{��%������������vs���|?�!~��sS��M8�<q�ٻUL.��]N�������绫��\Ws��E΅�6{驯)Oa��uWoiߏG��t�{�pZx�z�n���ۭJ ��y�r�9�e��]������I��{��ҡ}5s��r��ߤ	��K�ۇ�z��Í��Zj�}��Y/���н����{{�����^���I���pzy�>~�ו��8����#_���w�[̨H������������C��9��/2	�)�$=�er�S�έ�Ӵ�2�]Mۻ��)��vUe�Wqʲ�nSW��y?�������h9�����n��$�����'>���������Y�O�hӆ��i�w>��.fgy�i��)�u"����x�x���Gξ�������Q� �ژ�����oߪo�e�^�G�����A���~��z\�a��ŧ����������٢C�s�_����><nx�}���!�{��g�ʷk����ɭ�i���is����<�PV�٬�q{���INAn�	S�S���\��y��h�s���i����y�o���Up@�,ڷ׬���9hݾ���+�>���|�v��_N\f�(����d�ǮL��������=��w�T���mz�^h���E
��l/����k�u��r�/�\~�5���ʇ)���B��x�i�ɤ�7��լG��o�󃯵n�wN��.n����N/څ�\�_������]���M����9���ǁN�u7��y��&΃������L����Q�(��E]ެ��o��P�lIz�W,������)��"C����8�����(���aJ�[�4�4���>��i[��Jv2��1�վ�M�]t{WC(ŕ�j�G�σ��FCS��B����k~�/μ�v��_\�Ód� a��f�Q����l�~=��O_�h�ҽ����Ȟ�{��:�ǯ��:�c����oY��pĹ|�c�MW���pի�{� ǲNI���<�}I{�={���sL)�&�ݕC̊
�/�S��$_�dZ$)�֯�&���od}B�wzy|�X*�{}B�7|M�)������������"�����ED�R^��?������u#���?�?9���J%������O��[�=|��?�C�:�nQ���\�_�4�Q��6��aqn���7,�������J4/_��3�?А������R8���OvK�6��C�����{�n���/���Y=������w{w�|)��1y�\}�O�ću*.��K����=���L�BE
ṗ���䅎{���.��yrn�:F^4��t27���������Y�i���=��ww9)�|+��᜺,����Bc�]�OK����ޢ�o�ꏁ� ���e츹��冔�|z��k�#�{�����.���~I~;펮�~�7�λլ�r�󶦍߹�w���a��
�Вr��氪s�z�T�ay]���7�)��	vy$O2s8�݀¨�}�_�N��mT�7|��fP"`��G_��y{2}�N`��(��t5??�;�W��Ä����sp~�pL��o�x��nJ�5������~�-mu���6��*Ӕ��]:�գ��?FY��jS�a��o�����o9���"�%zs7�C�_>�K���v�gMx|6g��P��}��r|��<�"�K���b]+�T6��Or/��|q,�ZK��8�y�;v��)���ܼ���w���q�k/Y��w~�����o���������L�������z~�,���R�������������I�6���諞�H�>��o�Џ9������QB�]��'�3��Qnfy,�+��_�^c"�/\^�s�j�e�|Q��nU�q��{�V���O�!�����wG�:l�_�9�I�RōTSY�t�M�O��z�_���$.��!���a�>����g:�t�=�>�<,U��ë�������V
���,�_|��g��/ί��_��B:�á�/Jq�[��5M�+]�G����������A���������/83�����stӷ_ay���ž�e����89�DJ	X	E�+Y/�<}|���ϳ�5$e���>��ϟ�?vq���0�)ϳN�~|<l�������W���5LYO�������5s�#.���sSՏ�/-�y�7��B�^�x�������/�_�
?Oz����Q�z��\Z�i~�U�%e7nj�h|�B(Jif���H)9^ʄkuU�,E�>��L����Qb�S#Y��$�G_}�C�xGB$YW8�q ��5���5y��K�̳[˻^Ĥ���To1Nv��QR��u��\��ID	[Z�w.Ou���[z�I�6K��U�Tcή�$H��j�	M.L�#��r��.���%�y��"�Qj~S�x]"!�s���d'��H'�S�!M��4����Y�ku��ǡj賥z�)�R�kO��r%�w>��E�Rr��ڤG��<:-�Aת�+I�+�B&i�����̈́��"�^�%9��*����'Ǩ�?G�Hd�
�MW�Hc�y$�
�d�&��܈DǱT���؏;��If_Z��g}�H 9)��S�c�V^�#�#2_~HmCZ�av��He���K�p�R����t�!��U�ȦNiƜ�dr
���l*�J2A��\b�U���\��/���D�&�cXl�,�|iG���u'#}�<d{�ΌZh�c�f�K�,ʥ�pze��S05a.k�%�<?�^:�`'�����̐�uW���~*�H^���K�?�ettC�@;$�S%IQ�J&�I�}윮��N�,��I�2��-pj�m�3up:i�<K���о��ù��J�g:�쵬�B����ȣ���U��Ҥ�׳)�X'tuT����ҪĬ���bʄ����K���Y�F
=R�$C*�B�^�"��o����x`�\�e�dL���R^F�b4dk��ӥհL7�~���4\q�̻�*�L�HJ��P��n�N"�V$ �rs�!�-���+�I7j+�����`���8�P����,	N󢞗R�=U� =�����fK�-[*Ń:��#�t���I,��zP��t>�D�h���.�B>��C�]K:��"�����qAǪ�rg7�sp)I�'deBt /���a^�p#!Fp�]	:n1�w���IkI�sh�!wy���.�~�^�/���;�����U:��2�!�,��R�L�(@�X��dfJs~,D-�F�xX8w=V���d��mNA�]#��.F9~݅+�  3�_9���5��`�1.�)�رȞ�ȃ���a��0H��g9�e���̍X=x�?���dX����HZ*������"(��s���Pq��P�Jy�ւ�c��2Q�J���    =����S*���.A9�TT>�:Q��!i���J�4w��i�R$��R����L~3�J*pʃ�E���)�ң��hCR�Hg�<����EA�,�_��9��B�G�T>�������߾~�A\{��Iv@�"�����k]��8*�����-\\˾N�xdBR�<A	Y@s&n:�|���Ŋ���N��C& ����[���,!��W��eI�O��|�$��)c��N�a9�U*ǰ��9�6�����Pݮ���x�������ji��C���ta����8d�s����OǇ�Otd�N���֮�������y�Q��w��Q�tz�����{W�\y�L��7q;�������S�š�{x��?n�����#�+�������_���[S�:�֫1T�˷6����~����x=��_�t�;1�������*���^��'�xz%����ڤ�o�إ�l�u{�˗�/�KW��/��ӗ���A�}��:��B�ʂՠg�Cę���_*�4(s�L~���[�~��;������
��~74��
��b{��y��&�x�덂��JM�F=Ysm�~�s�sz��ׇ������_?|�����?����Ɗ��K#�GI�z���ϟ�ZD�/j���,�o�x���돏^W&�ҫ������ӹm'��'�D��������Z�<=�u�޴{��G��������R��N?>��{��^���P�+)^˿좂;�+�%zx�������q��mv�x����7
8Vn����
��^G}{P?�m�������3�����g�����3Uü7
P�"w���TgNNR>T�~�Iʧ+R|���G?��y��rN5��rR�C`)8)f��a��F���E8�%'�,�U��sU���1���(pU6Z�TcM��L�l:+��� ���%JJ�o=�iG!�&�&�p]A"d墌��)��+ɳ+F���8�%ao�Fe�u �%)J��(��V#�s��2�yE&u &�J���ߩ4Ur�#i]��SE���I�"����̥6)����Ot=@���R�)�Yⵢ�=���EN�Y���P���8z���_QpIGN��:��z?=�4�giu%��I����A�f�}��dLyZڧ���8SbQD��W�V�� B�?���V�p��j����P{��Y%P~�J��r�Jy��ѐܒFc-*-�6w����T�-k����Qu�E�Q���v���tE:?�����V�\"_�2(|�~P<_4e,�$��ԫ������}��1��#e�73�;.�M�E6Jy��їb��J��A�R���d>N��W�3P�˳��Ht��ҁ��ij��d��޵s��.^�a1g;�!1+:
�i�4-��ziR�!^�D�ꊔ	J\R�6�i�ÐR��i���渘喡/�$��\���\׶ʬG%Q�2m/�憅�Cz�t�Y9���y&oLE�^�#]-�+7U"���W��WM>T�$��^��R>Ja˚��q�-:;�c;i^��=l+�gE0[�I�������#^˷#��3�~�����٥pv���La⚤��9��B�&�J��~�l���[��ӈi�)�8�³�o��ju)�/��;�}H��ftJ~�Z�%]���5V����S��HK��P�>�έ�3��^}8?�"ݟ�,. 3৾N�CD�%�eN��R2�>��#��h��R!jP%9O)�lʥ8t�R�(�R���j�����+z���χ�+��
���F$
��� ep�e���ۃ#D�4���`?�^d6gCt��G	#�������,z/{Y�9x9�����G�5�2#��h�E�i�M���(폊o�U�0Pp��9}y���)�1�J��B�)uб�������^�ؿAS�dz����-W_�*R��TƧ�DX�޽�6�u�)I�p����x�^�Mۚ�|�A'L��F�H(��2VϺߥ��w��t�7��\J�z�:(��vCC)�D�_�*4ך�+Y%ה\��P"��PV��	� �z3�T�p �Ɓ���4��C��y�l,T��f�8vV͞B'7*��M]�$浾�4�-m�����Ks��
�5}[)ɛ)�Q���0̾M3�BN�N�U�%��	ZJߞ,�d�S��*&́�1�K�{-/S|�g�E
u�򾢮�����D����}�A�uw�:������r�G�a:u�H��(K^�aC�|�&}���Vr!�G�h����ڇH�M�_�Uu���q� �% H)U���oW[����i5o���tL�pԵ��m8�i����n�������z2W�=c�ߠ���}��ӝI�]u�E����#y�A�1/�}��I�^���7S�1�=:LI����}�.L�<˫wU���-� �7ƽ �
���B^�닙5�~�)̑��A��b=Ypi�S�w��W�gcT�Yz����M�;���5R�5��l,�y���	��������t�K�K����~y��aCT�*PH��+�	�{&lQ������(�%�"Ż�Ir������Rٲ��m�Z��P��x��Ξʪ��F/љQ�
'��2�V��OJ"���?$��Q1�]��tb)B,xK=,[�%E'���L�G'�AR��'%W���V^���U�L\� ^Aը��~&YF�抃q�����w�IP�� ��1jhp}`����0![M�.Ld'i���!���=|n%C�*���5��'�(�Gc:ą	ৼn�T���$=��o�-��+!�N��|�-%n2:����zQo�F�E7;k�v���az�m��[[4����	YN?�Xe}��E@$ցd�C<�x�>DJ�N�"�p�̖rdX�2�ķ"��x���U�(S(��V�}�\�u"�@c�Om�WLJ�N�_�?�%��9H�@]\@����D�4��8�0���p��&\I�*���)���xi^��ꍂx�x[������h��X5Ƿ��92T�e���О��8(3��ʰ����rŤ 1��z!kWe?d�k�?T`h�d�Qm�m��C��V��&�r'p�u:������A�@��T���=��
g<!�ӡ�j��� Uq���L���p��䕼��CA�\���[l[�k���j��b�܊�)z��8tO���k�*QQ�1���m��P#�R	܁��6$�!�� D?O#D�.C���E^���Ă�I�`���4^��5WG{ln�/9�.� ��Dц�"Ȳ��r�Z�e$���:�M���^\~ 5�8XG������U�qe:nWr��:R[N��uTN#}^Ų�+�U��Q�\�7�x7��m�F�NH+ٽ�J�]���a7�Fq�{z�/`���e��`ؒ	���l
�B�W"�uO�8����=���1	pPqh|W�[�#�+U1E=%��(]��X�������)���8|z�M�Ri)�4'r�0����˘e�۴��,�JNN�H�E�R�4����~�#g� e
�B9�f�Iɢ\��(aĹ�YT>��ڨP#��C���Lxl�Y��w�x�*u�N2wT.+�LG�C�+1R2�,T��34�^�("Z}���zCHRE�z�J��Y��V:�sab�FV0+H �AKw����~ C6mI	"Lx�9�� ��Ηʿ򥩺.K��S�\i �-�`���p�*r�'�����B�Г\�l��o`l���t9L�@"J��1G�49Ms#����0ո�A&�����V�h���Q���o%�+�;�<��б2T7R@�Ծ��J*����6}](5�C�n�hmF�ٶ�b�Q�d04�[����I�����4c�@�2Sۅe~E�~�-���I���(�i�i�W��Iab�	���>�pd�[&�O$�n��[�����H�Zv�ţS�/2w���4,5��{H��u�]��f#E%�ߍB��9׹j0�T�'����aVS���lu$��2�uE?2 �gBon��( ���2�v)��,c �r>��-H\
Lt7y���
�Pn�"�nt�	B�}�-9"��t(��1.d�I��RR�5M���pu�T�7�ls\�C��P�wM�t�>���w��    /z\T��xuHl�G�8�g��!�<��jIZ�7��ӊ�X�lJ?]ˢ�;��yySf�t��5��0�U"q��i�5 3h�J6��@ w��*��q��9r?KbH����>�>%
�u�t!�	4�B����_3#�Ǎˌ��0�B����"�mD2+� �����+�M���ep0g#UR�J+0��er�D8:��_k�xF�~�9I�Ì���mDQ�76����3؏��L:�� &���*igOْ<Mh]��v9R�l#��g�%s<��w��|�q��P��/L�j���/M�A��h�#�����Đ���
�\0|�"pklJXG��_`��:����T��f`m<H���]�.���1ܖi*����$�RI�NWR��>8�
�~����9W�'�f؅6~U��V�e��Sd���Uڇ=�!4��tK��LeH�z�`�`r��ԝ���as�/��������?�q}|~�<������<<ݟ�/���6˳�����������'���N�Mw��3ʕ����O�����t6�g�p`�[�~��~ڟ^��j��`�`����,�y�����_��ʲ��G't�/��G`�/�g��˫��0V��BY�`x��y¨�>�}f��7�nh���7�����o��W}Խ�]� j����ߟ�|V��OoCF��ߞ�b|��'����l~�6=r�&��2�p�%�d=�z||]~̨�N�7"�?W>o�0zo�3)�w!؍�����h��� ��e���oP��� i�oy:�]�P��۔��'�w�@�y��b��e���J�%+L|�(�ԗ�	=�!H�of��%7!��$�VI'`�KЌ���Y�0][YLa����s ��"�7�>(?������l�1��%�+oH�`�9�@i����k3z�d��9�O�������f�_2ﮨ�Y�֥�B�� ����YJ �+��\�z��"?��q���P`j�(�C&GpVѦ`u�A�ğ�IJ����Gk���px
V�/Om`���+G�N�X�<�LGG�(`��q��+�d#c��L�[�Nr��+�UK5�;�&}�
&�o:r��q��K�f�M{C�+�*}�5���Lո�	TR'1�&�v)�n��@´����P�h-�a�wf� m
@彺b�/��G. |:�-
V�@,�&}Bv�b�yL#��c���>:�\ �I���Wx^�+z>:�N��UO3���o��3�1�V�Ҥɨo<��2�|f�"��[ć�rQ.O�#�`m0P��� ��,3P�	KT&�1h)��\+m����R��()�U�|)S��]\8�uB��� B ��Wކ�5I�T:z��.uP��CN�_����_/[p���O��7��(�P2�$�t�HF�Ω �*��Ă1[ԟ���f
*'V&�I�.�g("�n�8��vۀ�2T7��+�s��2��T��l3�
F�R!�JQ�kA0�8iO�;ٴEϬo���SZ1g�2��s�8�9�J���.a��;OV��Q8�f�
JM�����y@�:�э�F��mgi3!�T���D�B�֌����G&�5�e��J�|gw���tu�)�#�Q�s���%��烿;�*��� b���&`�5J��C)J���[!���p��J{4����[ �
$�ja�i��c�8{H-�f�;����K��0��{�ڎu��n��w(Y��:@�R��N��g��ه3��5Ffq�)~���ʴ;��!͓�v�0�P�Y�umc�L1A���4���Qp�d�w�W�}�?K� /�uʮ�B%_!����C�-�� P��s��p�%��C�Ci�CI����z���(�g���	�,�Nh�h.��Kq +��8�?*��=�	��9Y���zeVonZ���W�H9�����R/|��)O�b
]$�P$8�t��o`����O�q.�ǘ�-����ޔB�eS�4-S�$iN�Qü4~�7���E.�/,�A_;K������h��^��X��͎;�I{e��>=4�7RG�ܯ�2޲y���4T�ʤ$3-#��TY

�<���8���
iOKe� @�#,'��ae
i�od���-�Η�܏V삨�D�U��l���:��Jr�2�����/,Be���XB��d���F\ XmyL�
�����/��Y��h̹0�g����Di܃���:��~5��PYC��⇁�l��6�h�:�J�­P_@���l�*?Z t�gƘ飵��A2\�����iˑLp榹G�+��P���sca�vM��:G$wO�f��Fc��M
?�%�؀dq�g�$�0�ALmIҦ�f�ݔ�@�-OƆwc�̅�,i\
(G5��,ɴfe����24n�r83i�fLo0�[9@����t�X�vt���
����T��s�})�D��XC��u�>2�E��Қ�1�5�a��qO�Ӊ����V>�K��;�B8�<.��6��%���ZT����W�J�4��d}&r��F�x]�c�4�fG��G,msĵ��+���hIcʃ�X��
��jx3�n�u�Y_)����'nV�dm%���YJ2�I6w��b��x1�Ԅ����	�F���!��!���4e6Ǭ��fC�J;�ع���偅��>TyT�b"��������h�6a୪�Pp�H.�ã�8,��θ���Ӹ��� ��A�����v�+�Y�ʢ%�Ba���- �Bf�CZ�� ���l}J�I������� C�ѵL~ ���!2�-�@F��SW���B#sŲ�KYS��V��p�#
��Dd�:��~��V���Qt�A8�~�DQ�����y\ <�hE�J�z���}��� -��WٰJ
�P�+����u�n���� =d��/�1�]��7��E&��dܑ~\�Z񯘊�vx] ] �h�с� �`����h���m�� ���03�3$�ֱt���<3�^�O�U��s��3�22���]	]c�d�`21��kOtfK��p�@]b�{��ct���qyf)34DM�]�9����h� �LF�?��iy��5e��'�` Vե��\�k�XRz+��B�hT�G�Bz5�7�e�\W �3�3eY�U�eh�F�i�bi��~f�"́��r��nƉ��FWn�)(������Z�(7�&�gʲY	��- ,K8��wt�SZ�q� }/ya������~(�?�u�@u��6��� C���!�]�u�M�,��"I��df�����hu�+�B:lqy$Et?*_� 5&�L��!�F�SRy�|
m0��Q�6�A�U{$�ʝ���\	ٙ��fY�#�I%-�Ʌ�X)Ybq�2纐��$���0X�󰻏�TTN�����bppk?���5q�bm9+�d�z.d��ȣi?w�Q#�Yb"Ci��;N�ƶ� ��]lΏw%P��FB��@�꽫&/�NB��/��}���Ce�:���]=��yw8ļs�����a'��V�C+��aŚ��q/)�c��u��^wؼ�-<����q���~��ݔ$f��5H��{��z�N�S�f��A���E%PKAW���z�7E6{`���(�Eg�g���Mm� �Gh�N�F]���'0(��C�����N�5/��>�4�-��U�`.|�P_��Thr0jn �<7�z&a'�aBA��p�h���u��=�EƲfV�P��Ra����|��ƻT`��4�=lHz�-���е1h����J�UR%0N���@�
z>��ts׀���(d!�.#z�)�2*�2���+q6"�{
c�%�h�Ɛ���*,�:��)����#��������,��v��lG2<uNH��Nd '�(�e�`�����UjG�=5��j�Bpa�'�'���Q>��G����4F���![��>%{YSߗ�t�R���=Q��t�&6�*�p =�{�I������0�9��2�r��D^P[b�XXzg�s�z���x��&����;':����    k�4 ~L�h�+���I�፴��`J�2��׼Pe5v�Z'��+$m�A��j���мΊj�K��ᆦ6�	���H�!Pf��&e���ڼR-� �&�-B�RGm�r���l��63��&���a��OG)�j�\�ڒ�K*|�`}�lh�]�9)rh��oyq�����n2s) �l#��\���JS2ML"_v�t��B��n8�CP�aـ�?��g�,����׆�k"��>�.،g��!4�b!э�1��65�<����pZ�!�]�:o^�t.�
�}:��� LJ�Q2�Ug�a�z�ڈ�F^�냮�y�#R��"�E�u��
�a�q ���	�eM{hr�7�йR%�T.�K���O�ā�~�Q]Dvh#S��"$[�u�o��\��QZրt`#����������Y���,�1s���@�	s��
FˋdI��Z�y��u�� S GΥp���0�Nµ��e}�g��[o�&��	����DM�o�,c��_�����I�:��c�R�tPA/d�=���L$�!]!J5���9P�b��J�j�k=���Sl��hV����J�l	7DmM2�S�Efoڨ5������A[�7P?�u
��&[�H"3~��	ƈP#�?�gx�9�X1P����	N���ϳ��вV�D)��0�����J�k|���uYwĤj'�N��$\v��x >��p��� A�'��y4�m�T���R�R�	\�Oy��""2�g^��rK-��-�Y�3@1�iC}�z�+����Q�YB۴��_���(Md��t�հ�0*j������S�}���е�	�vl��A�c��@��	�F�P3_d��}�?�X;џ��%/G?faؾ���聅)WH�(}S5��i��F}²��u��Z���a��IG@�<d2�y@�s.\\҉�cS�,v?��۩���;h��5L��,������e�-�)�iu�ԲTYQ'I=@�F<���ż?ٱ����uh=]��~����maL��GE�߹cf{sK`,�A.�K��K���Pa�h~e���lFZ0_]P!��!Q����,�A�]�mED�}:���Q��D$��%va����A��1�n/@?۳0��}�Y���oxQ/>PR�8�XZ&̥R�o3�O�`y6u�3+����d���L5�S���z�Mt�9PX֒+ �:��&x:��Me鞏�	���l��9�L�"��S�䩖���S������[~���	(�@c|�C�+VA�Ã�����~aV�/���sp��q<g�h�t����aB��V��Eh{:�盶���̊�~AQ��-�d{	�~�$-�ҒƍR�~�)q���J"׬�Uը� �}��8�b�;�� ���?�i�|�X� ��&*ÛG�ae�D��ZO�)�d��������D+�24�:�m�J�6\�ċmĚ�3���AS-~DN�>�郃�[v��2��R6��J��m�W�m���	�u�n�
�S�+"�a�9�y����͇�~JNp`#����mP�}c��ϟX�½G��$�/��6��ֻ���=�J"z����qs�)�۲���|8�a/w��Z�kx�awx���8������`i0�~��<}9<?����	'��?ll$s��ח��Y���O��珧������i��χ�����i��"�_g���Ov�n������φ!����Nrp��ǅOA������a��/�]�v�%�	�����	��If�w�>}������:�v���'}�˟��ϭ�ٌL�$0�%�ǟ�-ρ�f���mK����쐕Rh@&�`I"��n��r|s��<y��ph��KT���HFGU�h|ߐV����,�[�]I�a)�8�]��)fiA�:q�޹l�G�PWr������zi�3�m;������*�����Tնd�-V��k)��z��P�)��&'x���f�Ï��Z�q�7�d��yH�d,�BZ2k�z��Z�l��P5J�*+0lGZ]z��K�����.���+,:��F>u��֩ͩ�b9����X������|����~Ʉ=c!�Ծ2$��8sf�g'�sӐsZ��\2����&0���>78�7��x#nC�m6p�u��5$��QsKmg������e�5
ԗ<��1]sdfv�	ھ����d��0�cݑ�3�'�ѐF԰.%�\ P(+U(��10�
��M�t>Y?��=�kE�2�ȴ�6}?[<�V�K�٢�5T/�_	��0��h�K� I��!5����h������L
�Bݬ�S1f��S�T�Ih�+��9؁@�ͩLML�Ǟ�;1 �� �Ng6������hm@�N%cn�L1���Ԉ�l |���e�`�@��n6�i�B
K{�_� &I0�&}Qt�t29�Z�z��x�?I�)��8wdB����묥�/�fy�3j,�%q�+3V�<�J~�dC�<�:ȑ�%�MFE����T(a�d-�$�����x/c�6���:��.+,����v��4v�������d� �mW��J���H*�?��"�G'FrLZ���s���3�� �q��!ҋ�E�����Y����aI�K��?�}B]�'ފ� �x�5M�˂S�4d����:+�������t@/ͦ�1���cf��'���VrK6Me[AXYۿ����������d�$�[��$\���t'�C�1%��FIԏ���e!'�mgl�W�P< � a������P�$�J��A�0꼮�Y�%�`;3���Bb�Q*2��V��B]2�;q��%�+b�tg<��c�������$;�я@�]:�z�k~/���9��ݪ<h8��*I�]YĈ��i!o�@�AF����:�jܲU�6��a=�P<����3s�T{ ���!I��e9�CzrV�������Zd~�[fb���ݸ��e�i*�3��H� ��l̔��/�{��2Cߵ��I��%t�$,[�a*�V�1��r���h�X	�d�v�����I0�>�;g��Y	���E=����� �B0�O'�5��?��"�A����p)��$�����-�*�d޽�D�- �x�v[+y�9�Έ�a�^�%��ѷ�k�ՠ��q�R��E+�C���q0� 0�/ݶ�+
0�������eVݲ�[�@�Y�B9�cT0�6C�a�NKC����Ce�2��TiPa��͆Q��VBy���:5 HS�[؞�R@)`���`�/[��J�v���6F]�R:�*�!=�_���YBVCD��^�e\�w6�-t�uPf�mW�8P=��1b��;�ߍĖ[�<*�s[����U��N�ִF�<6�paˁ����7t�Y��:K��P�E\�6��o��x*�13s��bჹ���V��C���Bu��7x'i�����F�G`�6vn�F1hqQ1�ɰ*�j�5E�	!��Cc��,AU���<,��l/���o�,�T#\���F[�}���zg�4����<��ʯ��	U��gS,�P�>0.An����Q&\%�.`;�����
�Uy`#�`�D���Vf�G�*%���T.#��`Xs�����3�؋D���� ��l'uefԳe&�B)����Q`=q���\�����O�L>ѷэ�\([Vp4	�|��6�R���>i�	�{^�֗J��+�(���*�@�f�J�+�l ���K��c�lTA�� �JHiA�ނ�RXm ���~��s�8��/#�zv��~byX@�i,r
�s�@������@Ű��^��C7��eQ���pW�	��]���lb�yw���SƦ�a�s��坠���B�E�݆='���l�@ ԋme5x�yhMّ�@�(x�2@}.ků�'p���b�b��,�F�o��yZO���	-��>��������/+@�����,�h���l+x��b�삙|�JtmȈ㮖�]0�C� ���  ��J�������H�B���    �ԱC,K��R��Kb��l�F�52�/��3���� ��tZ��opˌֻ�s�T�(RsK�D����e��L^#"~63Y8�f�z�yY���JRT�o�;�ƕɋ0T��&&�fl�^i��wNQ�ƺRV�\ꂥP�Y��"Ȉk[R����h��0#C��X������xa)�B�n�{��J�mfP���#YAև0p�qg��_��Fs�V�,�+��㊽>�mޔ�f=�|�����ѯ�gZ���V��+O{,��!��{f�������˗/��m�����?��ig?Z ��\�z���t~�ӗV!���fĂ�X������N��_�������۲%b}�����_����7����s�+��.?����@����C��׻-,��z�C`�K]]p���ۧ���0�*E	�?���Yq�`�~X�r;E�`��f�pؙ��2^���B��3�c�@Ep��߂�eC(2������ے�Q:\v"^R�N3�o��\�S�$Xl���.ءK��-�W���Fx��,�V�Rb,6��e��<L���f�*�����2`�����
m��7��Qv ��l���()� p7�|�o+e]�D��Z�� �ae?�Y�nm�\�4vF��B�_�Y9D��3C�{�0fZ&X�+�HxAX-�z�3�̥RPb�.@{3L�e�Y�H)�uAC��$E�I?R3��FMo#7 ���LFOiD�GnBG�^�[��� []�^�t�.�&]���B�rʙ���,>M^��q{��d�)�-��(y�eٷI߸��ѧ|���=�FkZ�,�Xv���&���h��sf+��`D޶�e$�F�X��с�G���2Z	��K�Y�Hɖ!��$���[g�$hf
z&*�e�����9�$l}�n��W&
����6�k�}�e�;X(��F��3c��a5A_�v�L���~�w5� �e�����C2~8�S[p��Dp�P4[��i[�p&�VPtp�sokd��6ޚi��es*F��@'���̚���Z�s�:�U �gv�hs ��R��61���*�/+�B�	���5�"D�z�,a, �G��bX�̰�<2�t1�mF��T^Ͻ����'��ؖN �UZ�i-uN�D́顨	��W�'����t�/���`+� ���w��m�Ss�W���=��j#�
H7Gh#{	���0(<�*H���r%�6�Z�V2U#L�B�lEW
� ��i����+�D\L�����mM�L��Ոh�[7+&̓��.\?���6�T��L ���/H�a8��g;QX0� <��%p_�q\��K�Y-� B��Y):'��,2�Lij0�BSq#�dO6�rB�AeX����F���fp,ʈ�-�s@5���e2�Y>���m
�Ƒ�������Ə*�@=�j<����lZA����7d1�49ԗԒU@z�5.6��:��K��U�T
c�.[�.$y�np7�.��
)�[c��P����7��MQ��E��v�2��H+n5l`�| 츴*�8M��,mI��<&XQoغ������4@r����M�]Ye�5����i�?��Io�[�[b�z������hc%K�ɞZRؤ�i;n�3�'��P̐�Ŷq�p��i�~d�z.� �WH"5g���e�A��F��}�XZl������#l��Ej�X�"]�
'�M��CV���xit�̉��/8̾��#[�z�WЈ����e�o��sp���km�s	�o�1(�dCZ�ƫ3�a(�
1`�6�����j�a%�=�F�ᘮ���JQ����=�k ���{m�/7�L
�:���]Й�<,-m�rX�iX�o�4�k����K%Ɇ���Ys�AP��{M�0��Yy����o%��F\��,�d���N��|����!���%A�I��a����8.�G��sEgo�9�ڷ��\0vƪ�.F����r�����c�C��qi&`���6x�Ғ(��n��)x�3LȐ8'��*�0%��R}ff���������`�;cۙ�`ܞ-�����|m؞�3r�l�Yv�Ǩ��"݃m�0����j�Ա�qf&��R�]�0�5Dmy[;�g�ģp��w�'�P06� �F}�"�@h�;��`R��.-���oIM��� Ha3� ��=Ap����9wC��*R^���Qk|�3KX��)D�Ml���4���p&Bg�<c,��&�������Ǆ��̎GJ4��L��)��h��ݍ�+�%�X�w7X�ԁvr�5 d+$_q!�E���5T�M��*��(μ�}��.\��^ۤ w����:֩�Ԉ�4YK��V�j�p	Eǽ�����ا��a����z�e屒�vӂ�tݩ$kO�_���z�uS1�?'�ZZH&��\��K!��}��h4����Յb{�@�0�:��ي)6.ԥ�3�T�)���(~ꭡ[�m�E�;�?�9E��N6{���	-P>���9�	�M'�2�{�"*�a�V�en�2�*kXg���;k��k�S���M�9���\�9zm��$��2�պ��	���m3��"B��F���X4�j�M&�L�8�[���+3e6�Ĕ�L
��.q��%�f��N���N���9�B�XZ��6�8]�5-�b�k��(�f�19�f$k*���!�h_)f��_c�uDVR�esN��H}n�5|�LR��$i��U�?��T��r�FჱFBͨL<�
cK��>�ĮP��"
�1%ؑ,��'��l{�GjT��&brO~�a��Fb��!ݴ-�p
C�����#�4`x?�
�S���8�ֈ�m���u)��#��3̈-Ö�8�1/;{c-`ʩ��Ʒ��uL��,��@���fSv��#\�(v� �Ĭ�L,�5��(�,â��;B�vP^Vj�)�W�f{x��+!�#�Sx����ΠJ�7'/��ޡ+�
б(��%�3��2�B;�n�8Y׎�G���?z�vo�V�dC�Of����1;l��:��n4_Ğ,]D_yVV����i�N�('뵷�i��l�dj�Fw�̘(�kx`*(q6���k0�N`~�5�bu;������	b����9L�͜չ[��Qy��_�,zV��{�o���=v�Q�-�U��{�-���b��ɳ~��1x��n��%�G�
iس΄����(�(��X�/���]��$��"v[0��	��f�ɱ�&�X=��G��^H���9�
�6�Q|�0����6�������9fs|ɬ��>�bYàH��Ɔ��T+���`c�y���]\ÝB�Q0Q��ד�g$�����[0[w��f�.`~�@t^3�'?�0x�+$W჎T�!�K���y��������W �ݮ�;���^�CY�}ݮ�1�E�̫i�������������~��Y�v�'��>?>��1���wh����鞏8=��<�_F����F���O���������a� ����t���?=��*.h��g���FIu��
��]����ӋQK������|���}�<���/'�����^�+�P_����no�����kN�k6���z�k�K~���zx�v�������_����E�=������Yx�����u���rz��d������$5x�l%�����߿��l�6&�e�@�Z]���ε/P�}�g]�4����1��.!�ݜp�E��r:1����� ��:�G��Q�V���:���5��=a�J
e�LT,m"���S۶����������q�01�:�=C%O��b.'wj�m��D��5�)��GT�
����6Fa�%	���ru�1K��d�A�B/0�M(N�X��}��̭\�3E@?PnCv���M{�B���-g�Eg �z�Tʂr��FRw=B�/�f������9����䝶
䯽����Dw�IccD����]���L� ��p�}�Co�EbtG��2��A7���6���|�4�8��R�ӯee�h&�e��t    Nq�Ղ�3e�s��A1�j�7�r�Ux������ڣ��CY�4�۬��	Pex��W[lzV�@9İ��x�A��ή_ �q�$��XVz�[7���1��k��Vpz�Ѝ�A��T��7َ�V>�weו�,��^lR-�i��2��a��7Fx�k�k�r��&�
3[��p ��L�Z��ȩ�A\�-��I��2Tʍ��M�����"�
|�r��H��
-5��Ȓ?�d^Oq�	�Zتqmk��6��EuCR��Ύ[���xIpF�Ao��[g8�3����P�Du]М>L[L!��=�ef���"��ײ��-a]�L���P+dU׶V��G�"�!)ɲ� ��kʍ�^2����-�V���ފN0$х<V�%B����	C�כa�cpgU$vF�iH[�l��Y)]A}ˠ�Q�ΨeZH+�2�U�n,�Qt0�v��b��g:�v u2�����TǤ>�X��|ي��Ns�
�f�k�֥�T�a?"nOR����]q#������`<x+HE�Xs�d���m�gg%��l���4Z�0'"UPj�]~UJ���$����b��%�xf��d�p�(N��S&�o����Ŧ�%b���t���D�����Q��:sT�\�2`o�#@��lM<P+-ꕰ��x4}�8 �p�alh�?4�0g��9ފ�1��Q}I����Ɏ~��4�8`�`���	��Q�������/H�@�L��0M)D`� Q����l<`Bm��Y��΍� EA	-%�=��[zdt˕��D+����L�cxZf���,G�alA/X�B7��a��U`0YNq����>�"���xJy�R���j��NI��ݰ�^�Nf�F����M������aP���)�0?'���%>L-P��O3�G;�<��A�<ԙA^�'��,y~��v�*�2j>:�}��5Y�65�m���R�nz��m=ܪ�jgФ�P߇��,;����mdJ��=�&�"[p�R;�Řf���NQzSoL�;FQ:��S���$p/�C�B0T�L����$Z;R=;y*㨄{�^�w�>rVTM� �'�f�B�����A|7ٟl�f�u�eA˥@I�L	c��{ɗF
J�%�|>,@(>3��>�2`��Gc<�~�c�#�_��/��f�T� (�k@�K�4݈���پp�{�yj""�����w�G3ps����ж*���
�N�t�,8z6�����[F��0Q��t`��ʸ ���y��{	"y�?۠h���ʼ���nD4��3̃���x��fl�=� `af$uA�ʆ)�q����T��CB�H�Fb�b���I~+
�X�&�v	?�[wA�mȮƶ�r�N0)E[�7-P����vC�%�n6��
���^�b���?jS�md��CdA��O�T�T�V�w�w�JA����@����`�xXl�g��w��&�����+��,5E��Gmuu�Q�U�Y�(���o��ψd)Y�V.K�$�9���GX��]�|_��jh�q����aE%Ŋ�pl.�d���3�j��w���ҳ���K<Ox\��9����l�6r�v�0���u����c�R(�g�/9�&�綍�m��0C��ݱae��8w��N�#������5XO�&����M(�^��ɠ�m0'K�$�UIn����,�|?
��o'�#!ص;d�qP�e�jm4oD�6
�Yl8�k%f�!b�pm!u�	3��/��{,�[�@��(�r[�o�`�m�3�c3����H!�R[L6O>�gr�'����5��PH��k�%&
���(K���x[�X�B������`t+f�L�3�O�N+l��Qr���[����Q�2�Џ����aML�Մ':X%�'@�H˾�$�i���®���b�[�rcT`������c)���Q�O���-�'ƌ�a�X v}G,%���EVGA?�� a�P5��c7�<�}f�o��@>�9'�(�;�|��6 cj�±,��|J�m�r�m��H��S|'��1j2��D�L�<^}�Y��~��[`֤������f;�����WPH3�����F�~��`�s7�����80c+F#|45'Y �Á�n=	1���֖��8��аs�2�8��rV|��5�E���WcQg����
 ���D2ۗ��A��
`m�!a�>������#��0 ��|vc�I=���g��e��5AR��Rc-�0��M*�s�ΜXf  oڎ��/�=�e�E���ș���Y�h��٦��Xkqf�8gң��m�˺�`��z�n��ڙ���߳�)��5���5s;&-<Z��MFj�Ť��cu֛������l�����!L���|���'�ޓ}�W0�	�K`���;����S�e��2Y�5o��[q)�/H�'���56�R�$�cʳ��y��`Rl��@��QB�}L���E�3C�N ��i��Wk�S�̱��l���@5�ѓٽ]O�.׈ d�K�e�]`3C�0p�M9� V3-�)�*c�b� �ʻ�!�I�:�\�+�!�ٍv����U���\<�ͦ�� ���鈔"��'�Ό�ۆ���Zq�-"c4�Ԡ1IĒ�]�g�KG��d��YLi$�bۗ 8�}���J��s_VˢU��]�Me�Ѷ�\+e��?PR�)�PS5�L���qlF�6A�n����������Ì��A�Z�|,�r��}K��F+՛��ə@��J�oX�}/xM��-�.�ްBp��D4]��"L��	:[���f�U�����l�9l�3��(��M*F�hݜ��'����ffG�Ȫp�3w����_6��
���Mm����l���e��1�l��KŔ��h���1��$��u �}n:�@�x)b����˛ǅ�;]�,k
.r��k��?%z��;z\x�E���n��OPG�3���k]3�ʃ�%ۡ����>��C�k��Ͽ�S���j7����ە�i��n���o��.M��KY����*�cZmw���ۼ�nwi��V�K���d<������ק����� ��	82���oܝ���/�_�@��f����B��}ɯ��������e7�fy���;�v���������?���&럗��o_��y��������<��xs�'ĺ]^?�~>=W������������E�O�<~;</����Wn_�����BZv��O���ys�h�e�y��}�5/_��p??���;��w[��t��پ�t\�!�?=��|<m7�.��Z�ш�q��i߇���}[e�=,���L��"��/�p�A>eNl0�o�_[m�?�W(9��Oah�	��=�U;1-H�+�Vرlhi�ƃ=�v���>[�ZȏQ_y��_�_r]8�o��]������޴.�h?H֬�|'��i`��~�2����
�)��B�}��@A�]A�y̵P~�Q �&x��ؔ�k|�>:�*Ӹ�F�J$R�b�&���tHF��a�@�O�OPh����m�b+Z51���TR�
L%q���%�����Cf����P �ؚa��z�LQϥ�?/��?V_�屙�p��>)����+�MS�'�1���*XAu�`z2C b�j��|�U��/#[�ޡ*;8|�V�w�A	"O�H����&����c��K��26�〷P�,y.tep�����I%�:N�>R��=P�lWR�o	�$�¡B5\v�� ��Hf�[��.����k��:�`�x2K({�B�9�������(g��ʃ!�-���~�h
N�5}ßkPN�(���Q��o2F��y3 H-��R�$��à`
w�{�-��,�]�W���,����4��i|��UMAt#�e�Է�zA��8B�o5��<�dys�ր<D)-;@ �vpA���S�&ٸ����p%���(��U4"@e��~-��E>Ziwv��Ȗ�Ѥap�ͿS��r���cJ�لղ��0����)?�
#��v��6�.�6�R9�    A�+�1�j���"�V�UTx�l#��B���'4�e]�6�펍Sbd�6��Ad�6��H�r��p�!���F�d�]|(�L�ŏ���j�ܙ�Y�ܴQ
���eI��oV��ݫ�	��ۢ���|��E�f���M������A�-`�dI�[��r,�3�p�r}l��2�a�p#��hl
�
���
��ۯ˸��"6��&J�y<A���c�g��Ԏ���2��Qa��M�`����PY��8s�N֓bB�j�E�Eb���&`�����x?o��e��w����xd��9��Z�$�ΎR�X6��Y�����h�ع�x���3�x��ĸ�!�E�T'��|9��0[V�� �.�Y<t=�Ѵ�@)��u0K,3��j�yȸv�� �T�(��`S�� %D���p��1x!�YAŔ��m3v���V���jQq-�`"�%yMy?��Aꇶ��9�3IOeR�Bnm�/`�H�"�e����ői���Kn���(J�y\�*Q3ˆ��!�kcb������Mޯ��6�b��W�pH�ݡ�q;�߇ͼ�q�����v%�[m�!f�d%u��_��L�鷇��/g����*����~����o6���n��f�?����e��������Ż��iwx���g�(V�y><S�9Y�H��SpzzX*:V��m(�-��������a�w�g/�Ȭ���}��"�J���L���������fz���j<i^K;dyg*�`��U�10��5�WO;
=C�OC���b���@x���i��I�2���^���M<PM�kW@�*�]~�J2���8\hm#([\�q�v�����a�'���Tr`�c3���aKiL���ÄƆׅꯣ�sF|<�ԑ��'��ݐ�IP�'�2���]6¤Q;�[�M#��&�:���{���h�`c��J�ϔ2H�"�|������D��g���nQUҗ1�:w$Ox]Ri0%5����#K��-N�(��3e�ܥ�6~3�`�T�T�G��+-(�Tr��]��3_`.��j[�tI�i����Vsh�l��x&>D뮃�`]àSa��lv`�ʹ�mb�ӄ�k�r��z�6�"���9v鵱4<��;����	�3LTP;vgBO"�
#n8o7N�ۂu>��Xw
P�RlH�]�\��߂��	�3�\�ZH�+Z�Gyx��԰�MdɊ�LCH��!�N�6��FIJ��h;�q�o�I�0�ǎ�g2�`qP2 P>Z2~����R(9!�� �����-�������,V'�
z`M��+�e��'�ޖ�Wiُ�
}=��d%}R#0��� �sS�Y�������)s�)-QzV[S0�Yf~�R�6bmc�n�­�$����\gW��$Zxʒ P�=e1а�ٲ����� KE�[�L"+�g���p�
�'���ܚ�����ɐ\s�JQq�P�ڢt��z .��*[+�$�cqy��Ȃ�����{S�!gD��3�rz�í�*�C10��Q�y��i�ucwӈ��P�����O_��X����{���D�Z�)�R�K���,�r�]͇z�K�f��1��+q_7�fZŽ;��rg�����)m�Mn�~�����[����}�i?<Oϟ6;��z#�o����6�r����'E�������R8��z�k��]�:�����Wo;=헞�B���{C��6���؅�j���a_���l�k���>�#�>��H�t�J,ݰ��n�h9���#Y�v����ؽ��|��yUb����i�3���]o�����?����o����$9ǯ�=<.W��>���x��ܗ�����y|y8>��_����)?Ϙ��_�{��}|��6/�̩�5��S�L�ꎛEK�9;�G��8��E�p�|��1����A���H}�͊>���1��2� D�o�&�rJ`ܸ��ͪ#kz���-GA�E�Q�����.2�l���8�#���\��4��l���]�H6�)OIKQ��@�7_ѳRV���;��݁�?�+�3>/��)����:�<V,�e�u��N�������b�~^	<���Z��|�l�.������S
�4t���4�W���x�Ik��Ӹe53��V$Z�8[_���!v���c�jJЪ9��us[s������%@Vh�`�����W[R5v�)לA3Y�h['��M������Ҳ����\���S	L������W�� ��.�s+��y�K[Fa �d�ei�_�e21.kR΄[}�I�٘ұu�G��j�8�����_[i��g��_�&��e=����>���ɓ�|F$S�9���=�W�0���<��qɜ�qnw�[
*hS�mX��ɲ'��F`2I�3�����[��.&�v�@�>F��]Ow)�0E�
�[�գ�Q\������IV�m�S��*�~i� �% �T*���Z����m01� �p�b�o�Tf�G�A���.y�/k��'/����^�0j1�:� ����������Sw_�+3�r3�v}z~��E�C��>8Q�q����?D���n�3G�G��R�[O�l� .Tq|[�>1w�����V�#%F���f̝n����ii��Ų��s�!
���=�.���q��M;��H���ZCK�D�0��T�<$L\<�vA�'��o������d��.�����ǜ嵡`��o�ҖrC��X���T�^*s�*y�(ܒ��d~�9�d�*"*��eA��u�:�*�������@��<�P�M��_�C���mu
�>,5(DC�AT`�ѭß(�pƄ9m{;K�ScRо��q$�wA�/w��	���e�{`q����������+�pD�v���2���43��T��Ѐ|�8�@�M�!�8;���R�b���YsO���� ���B���w(�`�8W��v��^�W"uO��<�Eg��( )6?�m�:V�d���nEW5c�:����)⩄��ۿ�B��	y��f^�s�r�<Q$�5�4��^	5��Q�d��w'��h����o+����^��6'x�g����o
�71�dվ��0:�[R�D>'�#��-2�1��gk�د������W�tN����e J�^��tв��/���`+Z�E��=�{���ҽ��p>��"��b-J�d�0w��Q2`S��HD�$͂�V���|a�$��������� ���	����N��3s���(s>$�C�73�������N����[��E��:���<���$��i�;nK2B&��㍛��mĨ��0Z)zdTm=�J,)�7��(��N���v�7d'^��̑F2����	rq�b3faTs�p��Chm��HlنȱfW�a�ʗx�ߪaxM������� (�3-A�@x4C���A��Ej���:�f7u��0��p�i��M�,�<�: ś�O�ah;�Ҡw���Y.�<f�w�\:2N#[�T��i�#ъ݉S�����+�'�1�)̅:۽D�Z̤c�7$���Pv�j�#/��wz��n�;��������� ��7:b�^11v'���dK��k|>=���J�Ԏ�m����3�*���k~6b�(��:DL[�W��e��.�Z�}�O�dSw��gv�c֜`#��u�%or�e�-6Ԟ����B�V�{$,�@�3t!䛟�ֻ���E��:�pA����Y1��Sf��ĥ�N����nkZꢄ����ͯ>|߮��t��⤌��aψ*/��d,\E�>G,Bw8�Ի到�K{a�\�~ng��x}R�e�|�ݹS��Q=�'�"�C�����gӬJ�A	X	3�QH�K3��tY�B`�vo.)���vU��&���B�'	5re>~_�2_�hbZ�3�fH�n�,d�	*H
}y=@2�K�"���#G\�]ȅO��\<�QT�����~$��d4����5�`����NS]�������h�_�XA)#c`�M'�'|�x̸�'::TM1�!�]0��s��L^N��l�)M3�mk-#����    .�i��(�Q�q��9�C��o�����Vrg�K�Ŗ�7���+�Is+7��w�3�$R��%f����F�=���]wB"<����.����1�+f���<_���O�k47�#C�M$���m)��7��<@T@L�n�i���B^:q�V�Z�¤�~3��mi�����uKd�̣TRgjZ�}\��q�ЖXjƼ��P��^v��M8�gD��͕�z��P�U�poK��I��� Z,�=C��V���,��Y#�N]���j>4Ü�����ļ2�>	�s&��:����� �a�'����IVd�e��rbwzV:��M�GEH&��:!>i�XKn2m!�E�[�p�8w!J����]<y>=���r�iT���ҩ�ڡ����,�N�f��k�7϶VD���j掿��j��0/�7��o)�9��09���׌����l�Ú���&�3ئ��t��b��*�*��"��ݺ��%�5�Q�}����[��)���M���F�-v���T�Ҙ�R/F�D (=,+'��&���(�ȋ��~F'-���ie����� '�)f���[�}S&2	B�>~�����a��:�/����/�ڤ�)�dk�Q���~�ڏ�(�E��	��V\G���=��Q9��湔����o�^��#؞Y�i����X��3�{�M�gI5(���w㼥0u�D ����������Eϰ�nբh�v�A{\l϶kF�n�g��P���r�jw���F�hS�n۷����:Y)(i��,fSY���?��2���B�h���w�Nj��d���T:�%�U*�6��`'�>TA��ܦ;�QK�B��ځx�Yp�)�@���-�V;�n3u1��`+�&��"�[� ���ܭ�R�睆6�c��?S�zw��K_~���d�:������9�T�Rx�w�<�;Hm�?Y������Bz���u�O�/=�ξ�/=�����U<�V����,��� a~���h~
��;p�jC#a�B�%ʃe:)	4)�!e�T#GB<��Mq�.o	`����$?Kě��'�S�5�.lS�]V���}aV�T���0=]��덾|8{�香_��΢ȡ)@F�����KBM
%�,���l+�-�`(W�(\VhTi�r<�	�j�����OB�c�OSN0���O�a���>�:(5f\���,A�`�~�!��a��z{���dDgcfD��-�]��HgL��3�ӧT��i05	��+RǑ�6$��p��gvH�b��2G04��E|�b~^��=�d�z{hw�@�e���ʺ*M�/�0��W�/8�Y|L�;J���E�e��-����[pw�=W�'�����M���1��̑N낽\�NW�3���9��z:�@&~�\.��i{���1��Eʡ����"c������2��Q#85�aK�~�����AL�cʾ�n��4��B4�+i�0p�����U��jY9���o���U��E��g�K����#N�?�Ϣ}/�6��!���_�������2����	�Cv�"��ެ�q��䄂���L�QCL�,8ÏX���S�.���}��@dfUZ�Y���(7ܰT��l2�a6��
)E����^8�X`m�kc���'�@B��\���U�������-��ln��=��5�=����}]���d�Em'P�,�ʋ>��=/�}�`�h���pkЛ:�cĆ� |�ۄ/L�ə����j{|O��u�q����׷���S-,���>eu,�v���2����<G�7�>�+��S���JLa�GYU�Y!�W�&l�;�i���s[n�Nƙ�~�
�i� ��	���y��v1�]*�6C�	�p�D2;�[R�B_F�铐w1y*^	a!@��*m���yq��%ﻉ�	��� ���`���nAc#�橠H�ɍ���dذ9>�G �h�Ea��in�5�ŝ��-�+���K�(�����5���q��\�e��y��{�s8�vߏ�T�)*�C� m�a�
xydF��<y��VVy�r��Xo��W���DW����0;��"{߆�螑@!��0��<|x�p�c��@������t[xV��꧎�'Ƃ7E+bE	S��ioA~��m=�9+%1#r\�P0,�BF��%/v��T��o�[��bܞ.hK�b9�f�`w��ܴ�;Z[��w���"�ٗ�~���<
j���r�g�������@T��P�^�Xxa�o��������q��A&:5(r\��$�dK��o�	�4>�:���щ��B���������C~T���QS�*�,�G7]I�) S��bYn�k8��S�].�,2���V�[�<X��&>��gt�N�(L#0S� �'�육�RF�&�C�=�~,���d|K9cl�Ề��S]얝f��Y`��'���ؓ��2Gq��h�R�����X
[]cL�o-���@���}HnZt�1��<'�Z��T�Ouj���/��J�{\��&uݘz�H��w���>��u ����\��s@�'���[�=mrWR�Փ�n��*a�?��hխ%&;@�Iin֕,��Z�T�R����PY�T%/�����$	�Xg�	�g��1:|�נ�ܒ{�®Yf�I?H}��v�Rpn=;ЅeG�F:�
���T�ۉ}�nF����W/�.�'a�?�����\w *vMy��|�39��F��t��w��L&.8���^�<���\_�y"ӘP�o. ��rR#�]ͫTW�!෼� 9�^�_i���Q�҉:�53{�o�f���J�&��
�l`M�̨ʒ"��ܷ0y\�0j3�Q��Y����dip^��<bF ��\�/Ҥ�����S��H�4��:^���-.���
�	5Q�痉�ǌ93^�c�� �s��N�`�?#4έ��w���xO����LՑ�X,`B�`�B�=�1������"ڟ��7�<��w�=�YJY�l�����M�#�q/����M�xW�7����ݫǔ���k_ߤ׽>�p?`��� ��Ty���>>���>����{���'@F��}o���w�J� ߸!6A�8����z�Q�ȿ�����^��xt|�G��=��_��������<�|��ix�|58�J(��b��b��}~������@���[u�b�'���ʙ�H�������|EW!#p5�F�ama�'`@���bq�)��l<9���U��ؠ�җ�x�#-R��$�DT��FZ�'�=����[�1��~�sծ��#HIw���;Pm��m��\����xP��)q.S�a��Г�Qe*��4�{�D�~D�:n˥#T�����'���c���+�~0�T�N}����5>�|ͳYp�#���B�ܰt 1&XV�IO��UI��,*�2�hq�yy�C�j	��9���'][������͌�ŒVZ7#�$J��!�c7��#�P�}��R�w�'"��"O�%�KT�3���rJp0��w��s���a�P�P����P@��8��U�x1�g�FO�k;H`8���-
!74e�5�E]�'� �
9�Y�?��&}�Hڗl_ΖY�p}�l1yv��m!#1���~����0G8˘�4�c���Y���;��<�d�_\Y��L�6Y20
���u�{7$ҝ��a�!�
�U���?��Cv��i�0.e�TPB�ii��n�ߊ�$O
H��D@1h�l���hD�OayO+��2N��  '�C�o�XdO��wAb��CJ�v8���~�s�'Z넡����)q��S����=0���]�[,ڮ$�
O�A1�w	����DVa��n�] �]�ʮ�,�Ǿob���>}NW�W�ɐY��^����B����u~�+���^�Tv�f9*ue��To�*M!��c{b�!v��s��x/�J!Pd����X��7WҶa��NF�]�<?��t�	U�?^��5���։���5�,7��7kF��X������[A2�8՞�D>#K� bw2���ӟ�k��t�	�[�    �L�B�g�Ab�<EZ�)�ݗ� 7�ÊU@=Z(���R,đ�	s�y_�ϜQ�(\�.XӰ,tL�f�'���+� �`tH+�V�zGpm��%�a`Y]^�v!l-$�@�lǣ�a�ks6x w�<�q�� �"�1�(����S~~bN�Mj�iF�mm;��B�b�b���()���nk�tG-�,E�z�k�*!Fܙ7'ש2V�s��BG��.��{5��#%n��ӕ��I�Ű/���*�����ES了%e8x�	�����P���B��K��V��
��m�r�����
29�4���V�	�?6�r}�]?����H�S�1��M��h2�~��ǂ�1��w2�Ic�f��/��v�T�8�L��ǲ)+�vU-�E�_��sp�?�l�Zz��#�ͻW-������W��!�||b4��ۣ����㝝�~��S�{mQ��Oo��z�n��������^�2~��½�秗<������OoG��g�-T��zK�>�ѽ��R.�k��O'u�ߟ��������W������_~� fa�ڏ��/�~��~z���ˇ�>>�o�����>}���o������_|��W��Uqzzo�����]��{�����w~������o��~|��տ?����8���念p��e��>�����/=ڊ��`_m��?��|� G��[}X@t��}��?O�u�_��[[���>�b�i���>X��(�}�ԁ�-��_��^V���k+o����s����/i;��G��7e6V��_|����ڏ���WV�ǧu���e�����=�>��-���o�޽�OP�_��??N��W�ǯ����bD<~��C�Czm�Ǐ����_���?>����� �ߘ�����Ë�����ӗ�����3�t���_���{��������w���)6B�~�������<lp>H] O�A���b&Rq���o]��݋�6|T���Aʖ��ŝh%�
���κ�҂@�����f��`�`Q��'Z�Hz��0C�� {����g�宷�	�D��Rڵ\7�h�Y^��6�u��,��4��W��C�����t�Zd ��7�x�ۗh *:�Ec��d;��#D��<�?ڊNJSV���N�C�J�b�+SG�O��륍��I��.�ҥT�4���(�����Ϋ��Z�@��ㅛƬ�4�y���GI�K�k��Zanr���&0���l���͋�%LI&��17Ǵ�F>Mv��͟X|�1Mw��u{Ыgr�1TK��2[ǈ���_�g�!�@���L�!�Dc�򹨲����W��w�	��KK�v1�ӄ��s'�J�b0rx#�8�Hs�
�bQ��G��ϳ��i}�_�/�`����!�Pj�T_KI�V0�,�_�D<�^�(��L+�Ű����I��R�t��M�Ә�@-@�]r,6�����Fb�W���<��9�wB��Y�A�G��>#�dG�(9��,W9:��.�y��m��������#��F�P���q#f�X���D�>�+�m`l���oym�$�}���g\ �P�󡓲]qB�7g����2u0��<@mO[:�}�π&�s�t����*ڀ���궋�n"�1p��y}~��\�d��2�u�)��Mf{+�M��sP�,�KH\��¨y��^9����y���٫��V���:EI�o��0�Ps��<7uԨ�"�Y^���Մ�3t�[���&lC�"}tC�-s���%b�srQ��]U��H$)P~�TiYsS�� �H�Ղ3���}�����:xDSb��p[�6"�y�0I5���������I�F ���dW�Z=NÈ�#�j�v�ݸAti��䯅A�	7�/�@S��w
KPy%��6�uc|����2�!.�hx�"�M{�A�����h�������Io���ީ
ڳ���ذ�t0��hXF�T�bq��~�8m*�!��boW�U�UH�l7`�#�9Tܼ�}�#�~�c����8�:u�:���V��cHݟ����-C�:�
f
��e�	DȡS=�k&�m��/욢4C�R(/�KƳ"���\fL�l���
��EqTlc�~�t�S�j�T{^�����H���>����eJ8�}�L�>X���=���8�ׁ���WC����=���Ha�c��y��P/5Q9��4�Z��JC�FO2+苖�\6C�b�U@����I��[��l�' � P�V�4��$<��$��	�m�'X;�$���U�{=�gZ�|cLOW�k��݄#N�o��x�ܜ���7�m�hsj3P`�����e�,ц��ͪ���"Z�����v�c�`����w"���� �p�f?T��y%!���o�(b�%�_.XK�r�Z��Ӓ$��*�8�{(m��i�����&�@�$O����[�Y�:Tv�s�Ne&��`�:�}��1�, ���r�SԐ [4�0M�V��C�K������Е�l�_���k�fD;Fϯ�k:p�2��U�#��Į��s�L�����:�9^�/�O'D��~�=.ӡ��)'q=D%��K��w�_�	I�.�5'i<:���W�e�E=�@��[,:0 ��E��4��gniW���a���$_�i��#h��~ �}��fn�}�r�[I�}'8���4}d��M��g �4,E��/0n�tЁ�s�&���q~h�
D��j�|V9a��_�N
��@�R�0����5ZΙ�r+}��s�Mj�@�ז�:���G�(����O�Q��Z7����-g&5qC���9o	����PwγvQ��dl��fh>0�����j��[�Pd(�na5�	�:/�?m��x��5�����es:pB�s4J_�m�SE;R��w��[5�xj [*A�:�x��	#��^������l6,�ܑ�2|������A`@ e��v�F��x�:UvH>���M���-4�7�prS8b2T���a�i���)�)=<x��8?&�#91���u�&{B4,��ye�22F:��}�R�}� :�%�rU�G�U!	���8���ptÔ�3��n�H8���i0��ƕb�0� ����<h�dԍ���	}��Ap}���8N�c�O2��L����-��%�t��)�H;=/��6�  r&�yF(���3���7KqZ�a�H��$u!�cz�x������AQ��{YO�i�n�o��jt���y�Fx�����A~�L���lQE%]��ލ�<�mi
SI!E�lG�&�Q���Y[�6���Z�I��L�t5��5mP��ђ�6A2�M��Ӟ?��\�0�V;�e����Q���MɭfĹ�5�Z6�gQ2BqX��j���H�gW�պ�$�M�f�Ԯ�O�f��
��f3�Z�m�b[�mD�-.�g�C��a�j�D�*�Y��0�L�m�� �`c�%�=�=ZT"�*E�7ZN�PV�չ�]�M7�}��՝G�bkͪ+�ogR���({h�wu�����O�m�=b�"�z�4 8�Ђ"p;��'����7��Zp�ܶ3�\SP>�ץ���0v zLFri��p�r(m>2�<	��|k��L,���b�BK�O�YY��wW�N�m,,�v�^�ǂ��$�;⯾2��nC��$Y�(+}r~'��/��g>�)E�6F@�i�7�	���	Hk%��i�;.��`�厵ج����[�F������l;��Z^��vp�2fŘ����<@�k`ٝ/��I�Y�Q��.�f�!(0/]wWi���R��bI�dga�ՍW)6�$�������m4�+`���҉m����m6��3�����,��G���U��	b�� �?�42�5Y8�Zn93���Au���[�[�q���|J} P6�a��Vt(�v�ԟ�	,!� ��%^�]\j�P�S�+�ꄲ��<)�n	J���LY���7pj�g�r@9r3Cp�G��Դt%��F�Ы�렂�e��OX �a^M�l7�6��JͲ����6��� �  u%ذ��"/�&�c�hs�����~ �C�7���j��e� �$���W87�0^���>[)����cLy��v6�]��2�T��� �t{�zC�`�kc�S��������h}������)��L�������q�k��0�q� �{�9((0���R�p˱꽭�uY�.�_��1+GG�0w��̜�O�?!�`���!�j �B\1dH�t6pŒ�%[�3,-� �$�uݎG��(�`|P��ɹ[�P�k�M�ܾ-w��?Pׁ|ʋ�?2����,Y��~Y�^Uq�v�����H�:G����VȦ���dԋ�rX��'"�
 ��x�-J���O/bW����,��E�8��M�kP���9 _����Z ���{�ţ��*�����/� |�0�;1���q����*Y�u��VņE=ŧM�(_
�g��e���J琸�b`ě���>��a,���9Ez�XFmqn0r�R�R��y�ll�	O�$�{��02��"����:`XX{a�<ȿY����@��wOԡg�h�dy�Y��$���8�H���ս#a�
�N���6�P����;��n���b�%?�f�_��
��V�Ʉ�����քVC�n4���� d����rk�E&]Kp�o��⸘eqi���'�� #�-��D9�A1W�h�L ��C��'��0�@��{u)�s��8w��I�s���'9��\n���`�KR�zR�����D�r˵J��DO���2�M�Qv�R��;u@�d�a7o���Q�-����l���"�D�d���0��iL�-!�ݥnQ`���/��=��-�����*ז9����E�	�d��=�����sL��ߴ��P���8�v*�ţ�)v��w	>!r�����Ͼ醅Y�4.��!.���k�djD���~{��_4X�r:L��]v
�������ŵ��vd
�����B�֘8��		��a�z#6�`�h�������/:�����OD�FlV����J�+x�Z)�WP6���mp�Պt�u��;f����4�3�7���s鶪���8_��{��xٲ�Y�6�3�k;���5��pY��61�L���o܆��o(���極wɮt�7Hpi�~�M�a::m��� Dx���{O�ǒ%swn��]n^����E{��n�5G��0�� !w>�;�4ȥ�$`���P���[ka��j�	�0 x�2y6s�#`z."���qW��h+_�(��=rƲ��R+PG�h�>�.O�**�T���]1�
Yһ��X�p�<ʻ'J̤�uAv�N���$'b��(C��HAVuj���r:�Z!?C�C �p�=��%�<1��N�����;��(��z�ӞoD?�{(��љ|��x��W���mC�s�P��@6M��)�{�C�AS;�  �u�v�����Tۭ3��0�P��O�cG �����e�V~����~����T��      �      x�Խ�c˕��;���}�<�C�Ze2 �$ƼT��V�������FK�X,�f$g�=��Vv��S{=��|>�k�v��p����K*��o/��p��pJ�rH9���|�N�t9����[�8z��p���C*�̞�q�r�\����r=�����������_��˯�/�?���ǿ��9�8��ǿ�8\N?~=���O���/>��Ǘ���/�?������_~�����珯���.?���ˏ_O?��ӏ�?�t��?��]<�}��I�q������^�i鵞N��������Y��<��^��v�\��.�ޗ���K��z�������.���Irz-�����O�p����^^���/5��;�N��)u}�z=r*/1�����%��̃�1v���1���RB�t:4Y���~��r�Z�%��k�ҟ3v�1�W��׫�'�����K���R��i�g쮱S<��\����\��rפ��O:��k<����>�~=��s�~i�Vt����.[�~�$O��_�k���y���غ��XC�a�\�����5�`������[j���C��J��rɇ�O�u��CK��Q/*�dy�x�vѻ�/zO�}R��pz����/�����\��~�����6��>����ǚZ�c��w������غ'��B��ɡ+<g���S|܌]��rl9��1���z���Y.;鷻R�
�����c8�<k��	'�������{H��o��\_��|w/����Oj��k�᥸��s��I����7���؝�����N��//תd�\���9�C�EYw��5�k9������7�o
�f��{e~���0v��t~闃�ʰ���^�9�)��9�{�ӥ]���_�ޭ"��H<ɱ�^�ʞ��g�g�˿@�lo�_�Ǡ�۽�~1������k>$�-��]�Sr���Z�������7�o
�f��g��P}y�FJyI���ҺN���n�EUd�/]�;�~ϝ� �	'�����^�>����g�Z��<��AuB�������+�>?{�R�����M���ʳ��a;ٹ��sQҚ�x}U/��5�P�Q)�s��I���7����{��FZ�|�5��s��C�^��\���T�r	�W9�~z�v:����V��E5���������x:��e�*���Ӆ����E�z����]JM_�a�'���~}��D��Ӥ8�z���w�/׋�.����<�hl�/����莥�T�;��3Nw�U�t~�~��py=��{Tx���r�/�|կ�*3kU���1��5�R��漾gEi�>$U�;�~(/��CQ��?�7��w���!�����7��i�EOIA���Q�c�����<�d��{_���y���0���r���f^_Nz��T�J�u�宛��Z�;�����vN��zݶ�|Q����©��^�ɓ�̃��ݿ�BY�s��l���ED/�tUy�-���뫻�������w�s��5��#=��@�����_�g+�h�('�S�Ĺ����CIJ���ק��y�����d+��J���좜��\.�x�蠜hl_uI�bh��K;�g��_ko��zнL^�ŋ"��k�^��^�E���O<�c�g��*^�%#��u�O�k���]?��)Χ�.��Z���ss��S@��4����'�#�G�F����/g�r�(9�gO��C�ODe:A��9c����0�O8�����f^$��������������{��5��/��������ǿ������۟/��o��[��{����wJ��o���8��������ru�&@S�O�u����UZ���)�/g������e������o[O,s�VBH�'�����o׿�������%��\h��3^�����ǯ~O�T#;bO���)|��������~Wp��̧���C��?~���M��{zdW�OJ5|�E�L�;K��zV�TT�������˂|���������@r�NU�+9ĝ��J����B\���A�/��'����,�U��Ԃ~a�vf�εc��y�@�˅�'��^���t����+��+���q�v�U-*�l��osW�����ND�{C�'|�况����Z���Zj����k+;lǶ�6�h]ya�{+�a�y�W|x.t�~[Q������'���r�'!4�?�я�v������˴�`� (�Sr�t�S~��Os�c����ݑ������[�YN�j��&��r�2��Q	i�NF�S�pC�Q�W��'}J�v��`�ޛ�;�Y7�"��펫Fp9�=ǻ%�1ǘtZ��[���o��i��ᩥ6OO���%ұd�|�.���3�����^�9>��(��7�-��h�%�Q/��� I��no
%z%�H	����|:�!�Η����Ǩ��su�T��2,���~5C�����pQ�B��;�;뭭��IQG��J��Eݎţ�����U�ܼӥ�1D<��-�2U�����_�(��(���
=�ݩ(=��F��ΦP)�����+e0������.j&6L�BNU�V7LAD�5��Z����NBo���#�iL�n��U�������7��

[�uYJa"�pc�b_�nG���+��Q�%(��4��/�G��4���&��a�[3����(���7��^���=4�W�]�܀��l�o�Q��:�2������n���X�LOf�cёշ��H���Dt�K ;ї�-�m{�5�����%���@�m������*�ғ���P����������h�	�sz��1�gCC�?EŊ�o�G��s<+D1ї�k���B��_�MM���>C�RL�/қ��G8�(Kf�bSys9������[�W��Z���<��)\u!_Un=����6�?!��m��?�����K�q�:�O�/��\b�#-޻}���4�w��S�]~t��y��/(���=�c:��8�:ޕ�xw�
^�*4P�d]���S�'G����[]���U>�S�x�ް���\��tM��E���[��T����"�x}�b!��,"��+�r�y\�g�xNY�óo�9_�� z�=/<u8bǌAt����\�}K��%����B���a��4�(}�Kjdv�&ɘz�8,y��wF��L]9�,�]ж�V�2,�`ti��:Xʙ�=Q 6:
�q�80-�T��ʭ�*2=����Ĭ��⫗-)�B��ܜըD�YN��"����a�H$�������p.���΄^x.A��_�圙�K��뾨F�wQ�B��V0����T��To@�Y�%i	�W�� ���
5o
[��i�R��T���	��E������Q)S��RӕUJ�Xbt�d���%V�P�ӡ�4v���/@E~�k��98�!wU[
!�T�Cү8��+����z�����o��#P���&Rh�=���)�=����3J{�JV
I� z�U:iq�Jy��9"�c�~I��>a�)���M�
E9��v)�
^=��YWE�7���E˪�oT����Cev �̔y)ڭ��lE�#�����Ci��V"_h���7�ᩳ�	)ʝ�����ɐ��.
�
ú17��J<��nPHS�Uʧ�.O.�B�SÄ�F'*�r�kaqO���ʕ��������l*7�]v� �����P����u���_ƾ��"��u	k�ع=�n���e���\�3�";� :��~��U`��@̔7�q<��D=�����s�6
r�O!��7�?��ϴ�_��)�(<�1͠�Tt��Q�k�?UF*w��lt̔G�1Z��r<�h<<�S^��h�E���F�Sǣ�`-�F��l�F��ñ�!ˈ��q�p���~��\X�:޳΂}�ϔ#98t��<r}�}7�U�
��z�a�����_��[龍#f6yJ�'B��4s2&Kr��{{X����mfG�A�J�Y�x0Vg&�d���GS���z��G��y0H��u�UɩpG؏flT��N5��_gSGCU��7H�"��(��E��b	h���.�U��j���TA��e$�C��;$��c��S����ΩlV�3{M���sj�|F�I����(Lv:"wc~O�l    WN�q�{;PЊ{X���5׹�e�˺�J��e�n�/['�G�/e��,����-*�סR�_��Ј��N&�O�<���dl���󪑸�}���E�O���zy�)R�"��c��W�+�J�ʾ$��bM_VߵO���*)ɺ8n�C%�2;:BJJv�)�Ȥc�(_��AT���Fub�K��=�>�ɇ�|��pʯ�p>_�\>+S�v�'j�����m^����S����^���<�]��$^�v(�u=�M�D^\�21�P���^Yy�""D(�g�6%0�s
A�BL���&�`+�Q���)X�=�q)���e���&���p�GT���ɗM��+�`Iiy��T!(�,
npF��8]�=��>pJ
�U���[������g�κ�,����_�-^W�QB��ݍ=��걂����{�s�d,9��P5��*�ie-}�W�Mֲ��+�U(�6�^�F���el���~��U���$)�������o*]:Sj�!�r���W�O*���%Έן��$G{dZ-4_3M�P�>|��e1Z�ʳ9�!�]m��b{c�X�$`�ݔC�l���C�����C�Z��O�>�	�J�����n��s"���B�G'SA6L����8� %�VS�ƣ��@P�@W��lҕ�4*Uz�{(�k�z��C.�\�}^���}��#I���c����h��L
�ORI�}t�$*е�Ք��e���c�ڀ��p{L�0�xt3~s�%�b���mPF��)�l��Qvf#_do�:����$�A9T�1�0�k�;��HkDg҆z��Y��0��ad3�:[E[�
,��|��O��u5��nwG�8+���Koc/��3�{�� �ژ��H�C��1̢����_��Ff�UD�ҹ�,�Q	iڜ<����d�
����-o��O�D�Tg�[bd���$����t7|ʮ�½��_l8Y���qo%]�� ��8�`wC���s�%:&����ol�hi$��+�����|�<�~�L��+�OD�X�p�>���3�#�Ui!fUM���;�@7(�N:��.�;�#EI�����#�U VP0��2�}"b��j
���� �otRT���PtN�~�S�s[^�M��1��ŷ�X�Ź�!,R���[5��~0���S�mDZ��,������PJT�6�g������3���(� 1���쪿�t|������o�J@��+@)Zod2�F�Uw������n�!�&��l��1��#�P��a�x�:�pf�Wt�>�"u��TW������6��V#	��u�Sj�-�#��OՕI�@g����+���f�#������H��z ��WD�^(�D\�I/AGVΊ�/Ô��YǚK�ÞPǩ��Y�`i�"0d��!9N(�U����Q�/-�ӷi���I���8ǹ�DǛ�"{��{[d�r����\Wн�7�����Fv`=�3���ޕ0:zL�P�{5�r�ג�aq-�=���S�6 ��Ry���0F��K�A��*���YR�S*�Lf>���(���[���M
�CkQ�6���9�Z�Y�a��
��f�	�R��t!��A�P'��c�[M^�(���#.��T�l-lҏ��n�m�T������)�򦪚�{=�;��-����$g�dc����	��߂�~o,d%>�]cA.o�|?�c�4����b�^�r��
��o��(�տ�RAչCOK�q���Q>T�3��K�a5�dE��m�0;(KP��������U�l�b!Ax��Ub��,�4v#h,2�Bn�A3n��^7��L�\��c!�*dG�OJN��P�Z�{N������p	
'C��N.hC*l��	.�"��%.2;����T��(rU�ֱ�!T��g+KHe�tU�5��2u�k�1��.����մ�|J��JǦa!��p�J<�{�Pd<���+�a���T�_�<޸�e�{()Ǡ��n�>WNژJD �r��h�+ᗋ̴q1��*����d��	N>v^k�Kŀ�w<�
جC+\�D�(�s���x;#�	,�����9��t����U��6jԐi Z7�s��;�}��h�`E�[�VH%�G��tUB��{:�*
���[�j�(��G�@s��cgj����%�F�(�xH��0)�e��1*��x4�Fw�,��I��pt<!C�~����Q(Wh 4�e58�O ���?����حZ�9�@ |iTeN���ۈ��*Du�l2��Y�3k��|�z�h
�*��6�5�[B���U+�a�Ê?�����,���b�hf+����}Ѭd����"|h�gxWy:#pS�1Y�o�O��d��2��_��=t�@?,�Ѕ/���B�gG�&���4��{^ԑ�Q����C�Zz����(��NT!PչN;s�08Ѥ#T"sz¬B(Xy���e������׍�{�~L|;}>I[��}�V&'�.�с����ftF@FlG�;�ٴag�'b��d:�)Le��1i��2Т@�26X{��d?�U�6R��JVq�S|�W�bj�;@��r�=+X��qU�a�C�
�G2I���o,�{ܓ���8l����t�䥘�Ad$��jb�6'H�Y�����:��u��ӧ�N]���s�ͅᐥ�i�稉^��ū�=\.�xA�f��kVJq���=G������ :��4l��}��3&���5�r��}�`�S6����@*
�C��.�B�7���t#���4���:Z�ʬ�
Rޗ �AYqj�f��N$O��ʘ��E� �gr��Ʌr����Cw�Ne� ~c�1��+m��բ���(=�a���p,�OQǇ��>��T�춈ݫ@�:�>k\��`]��4�d�: �	m��g� ����M�)�^	�CkW���x�{?MiA�����o�R�?)@�c2`������d���wZ��T"(P�Z(y	y�K���L�8�$n ���YW:T��B��p���M[�x���o���F��m+9�E������R1)aZ+�@�?��Ԗ�o.U4��=+#�`u�.�֦�닁�������5�cΪo�W���KܗAY��_��F�U�C�	l �'�A��
u��юJ��X~���̡�LGb$-v� ��Ѿ0_��Oe:>� ����e��v2H���6 )hpos�v�V8�-���O˖`+[�v%��{����8���9�ޥ'3�D:�,�?�5,+���Xw�+MΓ�(<��i�!@���^GU-Vʐ�i�,���$2Ϧ��@�}�0Ra �٩Wlpe]&gk��b��8���x$��E�Ҕ���SWA��m��`��a��~ⸯO��r�CM�>=��<=9`CK.�����������1��,#}�027�Ih��,T�{�z����(ݘ��İ�.�����b��H c���"�'���g�o�h{=�W��l5�Ao�a	 ᡴ��E�{gU�[/J%@�Y1�y�
&0��5�q��� ���:eV&q@,{��5gM�JS����J��b\�ȵ-, �v;��� d�C�1rL*?��k�����W�;[ʎ����Ѻ tYUo�w�����{[3N������m�ȓ�0b�X^|N��Qٗ���sk�td�Z* ��)M��P,�*�{Q�іi�0��.��,$W�`s����@Sr�@U�l��L	T*��%�����r=�C���S�(h	DV�h+�������+�A�M�ii�#��f�d1�`�p^������Z��3��w���mCk��	���Jf"����a���mŌ��5I�� a�I�⭗�	�PZU�C�}�Ķ�D��L1��)P�0cgU��1m��ծ���L��atp���(���,<G`�_g���\�@�̐��U�i-/�*�
�a$����\a`��`v����f3ެ�6l&�v��`?�d(b���^긠�>�Q^���H_�<-�O�����}��$P=G7���x?��F���5�H�� �;q2��1Ĵ�ɘc��)2n&�z)��    �$:˓��W�rΆB�M�]��M���m�Hq���e��`��Hp,��o���ּ/����R��EQ�E������{<�>�!+,(��~��V�e�H�[�m����L�R��E���.�d�d�U�$[[)k����?F�C ���*$UF1P�g��-�RU����ͮ��{��̒�J�#6���D�#_~�*���QT���3������q�Hz��aq�`�ݰ!e��1Z��Ml�l#��J���JmR�<�������]m�7�	������X��me�6��d�Y(QOV
��TGꬭd�I82�6�w0u-�C��`�����7�t�V�iٜ�ց�m�� ��&�]���7�.���(�U&dt��_Qf)��َK&�η�YF�
���@��ͧ�M�@<�7ҹ��M�h��njY�|�ۤ���F�?z��F��p������h��Qx�ܝ�0���X'�e(�,�>^�����/`��#�E��x��6V4Y�f�d�5@N���SGx��\?�W��dOΤ�} �/؀��t0N�"��F2s�N!�����!]q�:(�WٗΗ���s�����'�~#+�&Y=2���v�Q�=�m�#sE"8aV���\�U�`����e(�2K��x�1��%�*/�[�G�'��YV�tn��EVB�NUq���p�fT�^XChI]l���[��ɽ�k�n#!^�"��}���W�B�ִ�$&A>�R�����%�gqG��-DOU�Y\��\Rh�/����N�/�m_L��`�x�i��Џ�5Τ|}��i��f��<v�	U\r�dw�Y4���B)�p{@eĕ�y��ǟ�$�t6h)ӧZ�:~1��Z��i�s����'�m���<��냷t���^��#�ج%�� T�?����Wr����� �Eţ;�Ug��?����,q�ߣ�Lc/�x�aj��A�C���[5����&,�K:[�G�0�Q�g<� �-tZ@�JX��,[@�қ��-9q�;���6���Ǆ���_��eg;�>sqn�^�Æ���i�:�f]�-G>x�UU������y���2���/Ƕp��Ckt����3����͗3!f�f4�qK껲PT��W`�a.���a��h�4�;yG�����������-52�%*1z����Eu��(���(+��l=p��(RL`����r����^I_�6���<�2M�WBo\�7xL�I�Pۖu��W���v�X�����-�Wa��&
��V<��ѐF��d���S����^\�=�j�k���^Y�0����G[	H��bZ9��*�nu_,���U7tc|��gAb���G��:S�)����i+Cn��`�����z�Q�,�nYSӳ���T�ٱAyݪCY��	�u�Q�:ɻ�b�����|�7�ۣ��[�63�=�T:�Έ=��0�!d�|]�re6�?���+�}fY�l��gG�Lor5�b	ܺeE����8����e�y���������B@�����@�b4F�J��7�lj�H�A��N2ꩁ�a-q�&as��"�S`����<Lȴ[�7�uM���'n��:p���ͣZBG>@�E��v��b�m�:��x<�����}����P�L:ښz�{�����<n=؁�V^����=�� o�����;�9B��o��Y�ZY�m�T�(O3�XQ�h:TGm
H�,�UJc���V3Jײ��o��8�3���6�5��]�>��q��[�q�^y��J�S$��,�7�L_��P�c���dB=�/�I4�:��A�����6E�G�@\���)zvuC4����j��)3��cF����a��_l�)Æ����!�v�(=�(%G>�ٽ�>�e���{BЊá���1"Pek�*�j4�V]�|�����ݫ��a~�@B/��!��#@��1h����J����a�U0�}�e�-�HK5M��UB�k��In4~�"�
���FRj�!ƻv�"�'�|�a˯�Xz��]�� �ۖ:;���A�X�T1��am��m5��h@�-��i�t;�)�]�\��:u=:��a>��'&(%sa�݊u ��Y%�sׅ�$��,�ot��-�F���᳋!�Ul����.�GU�D���G�~�N�=�k�s����?W�U�-��Mt����z�\�#l��#�vq,��͇w��L������5�RH":J����x�w�����0�L���v�?��;����T���[ ���!�21D��6�}�w��E"set7a��`%X&F�-�Ϝӆd�l(K|Ȧ|��7�YB1Z�w6�ە0�ň:�F�j�mB[$�H�����{�2z�~����|Ip8�t�4 �ȹ�����Nd�#���N.F��� ������Y`cp.ª��">�E<e�Z�ԍ�w.@@''xx �R�4A{,�~d (/�%x��"	N=R�Q�1�PT�:��(l�jrp��&	w*8Ʊ����
�����`cc���!U�Ъ@^JYOl+(�ì�k� ���>R${��k螴��M3%0R����I	<Cf�(ӦY<T�c�}�.��&�e���ΒsW�jǅ��Ix<c��~���)q �,�Fk�JPm�J0k2�7�|��P˭����̜Mô���c���g(�� W�b��@-��C���NFНCy;�D�˚�gD�Y�y�R����]!��\����t�<�W���hۃ�$J2�&���=��  ��`�+���j���VP��*��"P���x��X��m*B-_��O�8ZJ��:�b�CkkW��ف��h�4b�a��D{�!�C^���p����KlNX��l�C�6�ˊ�!��C��0;�wV�gb�Xe�upty6�Ƹ	M^��dqd���X�Q#t��e=�Jǲ�gy�R��ة=cL�p�^U`)̬9q�(���c�Fu�Q��� %geũ�[(<���:���Gf�*0Z;Y�HJ�B��&b�${y{�X%O������z�
	=�w3Xg�?b��L	5���㵽�@ 6Xf��&}�B!��q�!W�L�n�����;������*vS�c��V��]��n�t�T�R�0�ޠx�8��Ll����"�L�E��n\�sB�����lz{4��aK`�چ1���n�� \V�#�{��l�����_PFLRF�l�e���<�G#i 	jj�R�.CT�@�ù��R��_�t�v��x�H+�#�P�h�۲0��wӋ�.o!���j� D- :�`{{l
�=qH`�]��o�=�-�����	12B��0��4m,�Z]�����\�TB��m�{c�VfY�Co��"ߒ���F�`�+ q?5&�[��B��ۃ�����6��,U0��C���l����u�o�*eɓ̎�����Æ�b�p�l�N^zS� ���t}L�zҤ3�B����A��`�m�M����܋"P���S�{K�dӝ.(B?�_ĈJ:�[��j��@Vf��^,.	=V�I�}SҦIb9��OY�GJ�2whlQT�❲��薅�+�ÙŸ:��S�Mg"c#�  �DQ�W�� �'�4jv��X�������ΰڇK=��v>�kF	ޅ�;��� I�/�^/)�����y��O%���
����Oۧ������;�=��r
����.Q���KX6�M��iq�����������t�M4�p�	�Q�	2���qp�m��������fϔ�WT-=�z����F�7v#���5TY[3YQe�	��/�x���B`
��?[#uV@]В �3tK�d¥�c�����-;1�o�+5gD`���mvz���F:Ph`��2%&	�0Es��C*��U�ݩ
K�w��@�$�@p
����w�3U�a��f	�x4V|
6$s?:�s"c�m�ЦM4p>#�`�˪�{���y݇A�u����
���߰B�g�M����|4��հ�ޠ����P�f��#X�Pg����|h��(~u6��� }�3���[�3��/|�}�$    8�%XP�����/�Օoy��U扬"yv�61�:�J�kH��¤�����΄��J��@E�����u��|<��&ԃ�S��Ū(X-��0y��,TDz:G��yeZ��U�l�[���(�o-����J���7\Q\� pf�yui�o��-�ч$&-��h8�I��L�ʄ4U�HΤz*�q`�5�-�3(���i��@�e�C�U�)%a��t ����7<���|<ÄJV;�T�����Pki`惬�c���4d�T��=��2���Y��C�?�+q�RjG����D�ō��h1����-%���n��Da]t�j�a�	��
C��[���g�)D�����č\:�����d��D���^!E�d�=�þ�Ys�熸��`��?:*_�������B��ذd� �ۤ�?k�t�� �4��Uurp�$�-�E7��h �3�[M�!IWH�ݴ�@���8 ��KgM/a���ۮ�] r��*���<���j�w�R��@pLe�)�W�U�	�o�2���T�=#��-�f�QE�2�ˍ0��ٹO`��Ȍ�)��L ƀ��V��Э��A�M���a瀑U�1�f�F<t�!##<In졐���Dy�����͘$U&�[�2�og:1
��C`9��GZ&�Lq��8����v;0HMc�����5�\�C�����H.������,�ߕ�eM
%Ҟ6G��fB��0n#���-%<�>�T�B+c�A2��-@��3��Yis���m|��`CƘ*{����j,l�ӈYa������e#��,��10ţE�7��{��PVP�������J����tB�/�4����CK�����G�,]�]�`~�j���ј6�<���I��c oh�;TG,0GE.zc��$��*���hM0y��7�Υ��g��5�2C���J�mܭ'�TP��,�����f��$"#��}�^� �A�N�Uph���8�����
��U�Ҹ��ۚY{S`*�ܢ�XnpU�$[�fU_)�<�z��)��&�3E���L���^�*�H(�piYݣ�<��6�:��� �卭��p���sXC��"�" ��3m�f�+�[��H�)���>*���ޔތM��`�dP��0�,��{҉�d���Wbn�g�/$˙@1�G {��,7��G��%4�HRF�M�s��Jhk��f�C����-5����H3���~�r���$���*��Q�itQ8F6��;�X;ؠ��6o��fc�䑃��QSЍr�<�N\�6�_�y�A56���AО5�������pgU�l%A�7��G�O�N ���Q'ѣM����6���r(u1acS�3\�S�4���2��T��V_e�ra��&3��$��Wo����#��z0�<8�2�K�1���-�4��[m�#��`�pM�N��jTl39A;���7��[-��W�̿KB'ػU�C��B{��!�h��ϑ>B�J����`s�mm��4�i~_��М�zå ��pǸ׃�u���9��ٹ��	���S��:�"���I`i}O#�"P��<U H #���&�M�T���{��V�k-�$�Y�>6|
��	��B�^�g���#��)�2t�-P�TԴ�����棿��$hm��	5@o���P�xW8M��A�D�cr�X���s�A�JX�{y���o����ی���lE�\ح3rB�)Ƈ��X-�+AFd������R��Ww{E��$+Qٜ��h�	d��D\X8�Y
�{F��qkm�Ԟ�&�ϩ�0]	F����^����h�����(dKV:kP ޴8�ԚR�@��fř����\�d��E��^�m�Hu�;�"�%���@@/�X$�Rj�T,�ɹ��V0�!�Eq8*�cax�5Lq/vĲ�)k&��>5��Q��Tٵ�T�3�@���*`7s���f)���X*t��h2g���6"��T���Cyč�+k��,[�1(u���� �W��.�\�YN��D1��)��	\5Z����)��Y�Oi��5�V�ٚdT�i� zB���`���.,0|��Z�8X�\E��_+���vb���X���J˒�IQaൕ4_f��NU��J��r�HV�G�A���O�m�Њ͂�c=%�h��GJL'W?nz�1�M��]���|-L���,n�A�\��)A��#	�}�sHa)�4�� %��hy��IYÑb ���Y����F��c�����.W��59#bm��3��
�%⒑��yq%�B��|����A
�O0%�{��>]�7?ֽA����<z�B��3~�ݦ�j���Jà�a���LS9$R"�Y�֙&ʈ4A���a�-�Y>p
_�]XOa�R0��&�½��m�B`��)c�F�(��/'�̰P5b=��"��a����	�#$+*ohTi.G�4�=���3@f��s{�3��ׁ.���[���XG��J��O-#�"8l_7�B�=����QS�^�uS�((�jl_�sZ�|٨��7����M����(}��+(��M& )KU��Ϩ
���V��7��u4�fD6� �+|�'�w��BN'�4���=i6GbA#!G��}�\ɚ\�����R-�جP���C��Q�&ŀ��:XPSԍ�yt`��37��e�f����9<�z˞b�io�5�4�Ѱ#�֡PM��i_n�vO�[Ս�m?yf��/c�-.��^�7�mH�<Mb�^	����4jEwvŐnP(��j.
��r"�ܝQ�\�jΆ-1I��c`B�ܶ7��#P�0d�-����'�-C+��d�㹈G ��;�9��~t}��5z6�,LяL`/ňؗ}?sض�R���Aؤ�^㩟R:������|P��r8�K*�����ÓPԟC��O�����w(j�A��|B��V�ǻV4���9t-Q�<R =�j:
�y��1�@weV�35�MSf�*��{��h��LIEX����wvIq�J����,r�7j(CAN�ն���Ţ�f��r}�BB�L�۠�n�wP�C}a�;��}Bh�p۱/E6�UK���
����N����"<H�#H`�n���P�ж<�G���c3�;������m�`���]�Go�� �؅w{�D��޳���ߣ��3��� .E���S�ͥ��Cg
)F� �H�Գ1��0;���RY�d]e��o�L4*�L+�,pL�r�ZI��6&˲)�j.�9�����I����>*->�tT"���et+,������aL��m��L@[���NT��6&�i��3
�˱>��tI���;�)����І���#�O�lw��Ѥ�aT.��:�B�0��[w,�Хa�'0:�r��b ��@��fOC��1�ҏ��m>���t�=�1�ȵj�������6�L5�0]l͸��wc�pk�l�����=��eo	U���|;�rP��M��-ӳUۛ�ī16��\w�z͆z��G�{�Y�c���c� �=�X���Ӣ1ͮ�FۄD"�����J��S��N��!��2.��Z�𴛌j��6^�b]�Ǯ�Q\7�,z�F�k@٬!#�~� `W��&>\J{9�-��A$�a U�Υ��S�Aѥ�-;V�&D73�@Y�&=�,���~���(UU���e������%��r���K|��|=�Vz�Zg_����	>ើ�L:����_^鵝�����E��Ž��2�g���k����I_Ro]�|)�\��5^_��D[�r��>�`S�Z�^���=�#�)�|�o���+5���A5�吂;�2��ؽ�(�<՗��E�T��t8!d���|>�C�|���]����.�2���};Z�[G�b�UU�]_U�����!_/|Fo����_�kL�{t��^��tЙ�]�vu�5\��ϲ�3��_��1w*m*)�\�}.�|�˧Ad푑�֒>@���A4�:.�̵��a&����7ݥ��m~���.B�h@�3��9�    ҲvOz=ࠅ��6p�#�}� ��غP�D:Aܻ��ۋ�X*ٻ�n)k�����
@�����J�᱕e���Ni1� @u�9�#��U5������RO��\?̏C-G� �Z��7����ah��e� �f)`� �@������������!�5S�-�$���%�'�
2��hT#�w3�����U(�!���E��(�2F��p��/o|[ŝ�,�v��������Z��FpHf���R#��~�I��)��nkI�AH9s�iJ���/��"��>h_X�9��ib�\k`���|gl#+�B��5�i`W��9R�ᐷ^� )R!V$�ؕ[�)��~Y��;/8M���m�ݐb������y8������p(v[8a�y1O�s���6���x<��pM���{��0R�U���%��k� J&�G��7
��3�v,���7-��z���@ �޾���_�/Kͣ��/؞"�}As,P`c�Hv���aO��t�KmԐ����B��[��F�  �js�s;�hLL�>䄠I��x���@�!R
��߃lk�g�x���M:�P[0
���̥���L�`�},X`ddg����z��� SIħ����d��5���!��U�þ���yBj3��U*��0��`�u�i��� u6�aCꮸa6]���GK����M"��Jj2��ѧ��,�1K�d)�[�I��x�
�	� �Qv��{##en����PɛO�����\�}��4��y��8��l]6FV�-�? i�Ȱ�f�Pê���o������H���Ew��/q��� ���s��A��0hRZX�Սd�
�� ���ZYU��3>�p2��� �p �� �s�ތ��)ȕ�I�Mf��dK�U�j��'��-�>�������\D��_���ȷ2�Ȯ����ѧ��1�m�ޙ�9�:����na�;;�ϹPXw�>���1e�,��
2u�a�:ظ�g�~�1~��u�-e��?6o=h)`�`Zc(�"6���$ɐ���sE�_#��ԁ��7;�G`�Q���db��$�D���s�ʍ�,���Z9�h��ʴ.����F?������AZ���|ɚi+K4v��Qd[6��&h5=�0r~��C��N�`�L�w&����!<��r�h��3��-+ L��68�K[�2�C�fң��N͝��8���L �sl��jO�3�AHRo�h?h�m�w�{�����Y����\~X�)GY��|���Ϯ���\b��"cqSt�@�!�h+*K��7���4��1��7b�O��/�2<��������2VXXt�}v�F$�=٪C������ή��f��7�Zᜭ&���j�F^�Y�M�Ҝ�B��E�U��y|�7_�S�����.���\�'��6$C������x����%�}�5�<
��@կ`A�h��?ֿ�W�(נ�IÊh� �ܨS��$(ٹ��jgD ����� 5�n��)�����_#ch;��?���V?�b�f:�:�j�fk���1en+߱!��4.��d�p��^��F7��~�wK�ʜ{6��~^V �P��#�Q���aW*Y��4]M��/ *j@��]�B6�#��jԖ�8��,`Rnp��[�(��UҐ	����z����n;M@ޣ�����&���]L�Q�wf�	+;(��p7'�D�D�N�X�l$�-�'�)ŵ
,��L�#��`�z�mOhi?І�0h�·Önu@x"� �+E NVA���u��XY��G��5�1��bjACb��|���:� 첱|̦$ꕱ�IۨHP��'�=����9���<�[���ݖ�݊�Z�ƞ����p��*�*y�2Nț���r ^���q6k+��	�;���[�CB)�yo��W�%kg_0����1��H���P`Y\�v����4�ힲ��A���*bP�b���3����u˻n/�:�'�9*ß%~a�#�%�	�a,x�C��J�
���a���>`�M &z���+���`C��z�!��ד�Y;Zw�m�9XUY�1}�ɓ�`j�a*(,v���1�pKܷ9GG/����ƺ��IgՔ�;<���e�H��k*���u7�-by��I)a����⮒�mUN�lƖm,�7����&c�����G9�܊��E�H�M/`���2�2r��^PH��;��� �P1�6ٹ��ˁ�5셐pߞ�n�1�(XM�ષ�A��%#+i�� Y	2+S,�!��hr�8���V]Qe�lu�����X��@��X�Э(S[4n�=��u~Q�[ �L1����d��ȻrBfz�
�wA�SI`���Qه�?$ۺ���͖�g���*+�Dw�A&�-�{�eE����,�3�����I���&2~`V1.-Qk�`�ܮ��7�P�l~Oa'�Uz�����+�r)G�8r+�l�B��L5C^�qXe��ǡXQ��J�R`��m T�!�J��������q�An���O�ا�ng�V,�N��Q�J�i���A�y
$�㠧�>h�B�H���:;FQDvaK-n���V�i�Wl����Fd{e���Q"2�����۔to�����^��.��r�yYnjqT�� �Rj�������(Pr#�'����[d��U�0�ZV�Z���%j�A�1g�R����k��blhϲ����� k�Ʋ���<؜�����g����6R)��CkswKp�+Brs�h�xFk̛6��m�(m��y+�<(�U�&�=�&�$ Y��w0��6E�l|%1�/d��^���TN�{4r*�̓��aj�- $���l��*0��N��1�ӭI��a��=@�p�o�v�r8쫢�˚i,a)����y�Y4�wt�x�Q~�W�~|e+�n��CB ���w���h*,�R@DAg�	f�,q�_E�����f�o!_����i��Dt��2ݑmK������"���m$�֊e��3��`�9�?������s��J���'�4Y�6ӿ��U���{�n��zv.�9����_����,�4�g����֐���\�v-aO�8
$ht�2�.�y���P�-��	r�rG�FX��
�e�<
 ~�}`_��F*Q �UD16���&[�3=vJ��,۟�	h;�0�ƀ	�-F�<�<���C�&�P1�I"	W%(��K��
��(7�;��q�k�V%�stP3��as8o��'��L��%GYz��3��pT%m���[Ó����J;�X�-�DLC��V%����]�a�|7u��S�Q�p�����f �<�7:��iF��1�W�5�oh��h!�R���0�8j�;�Ft=`��(�%�&�;�F��iL�AŔ�i?�	�^��Y��je(JQ�����c��`�5�8��@��PpF�iu��-B3��}r��B��-��hwv�iPQ۶�q*ݽ*:��H���w����]��z��7��Z�,Qw�6)�	(��6�I�����`:��)� n��s������,�M�I�aFf#Jbwj�Ueu+�j�9��'9��疀�/�����m!=�Fh����3>%vP�{����V��C�g�3��a	�F��u�x��hl�ͅΓg�!�e�dq��H�P�rJ�Y�ԧo�9�2J��`g> 	�DV{c��t������$#�������XK]!����mU'���	4*����q�z���?���]���ӇM����͔P��um��xF	�	�r�V��L��� �K���=���T��-�dZ�]��Eh�$�;���� ����7,<[�,B~�����"Cg�� ���;�Sb���»ŀ}�w��7��ݽ�P�^���j/�'�hкuc����̬�̕	�=�aoFֹ���7����W�=,<y���zT���5^�;A{�LY�E�"��2���q���)�M���b�)Y�J�T0�@S� ���,)0( F�vC�<'�j]~�� ��ج�N
{���{��~�HC��n�=ζ�a5u�썻{R*���S�<����(GFiA��I(��x���ɶ.Ru���1~16��    �"��L��:4�O�~� T ��l�bU����N<D-�a��3��5���=sF��J��=���o� i�T��wM�;
��py��~����\.9;���Z���K:$��z��T���xy����Z{��-��~�k˥�,��Ri������ѓuZ:Si�L�~7bn���$���[TK�؍e���Hn�B���=q��{��0��aa^�%2=f�X�;�V� C�Z���?�#��,�#���4*R���[H>��@{ \�e�C�
`�ɺ���!b0�;�0�Of�ס�7J�w�O-�/l��`�D� !p�P��M�`N 3�$������Z'ֹ�����Tv��٭�Vl���t\A.��V(���34��l|��� sԍ<�",2ʂ�p'-�+��E��o��<1�Q��j��(O�ơ��$]�RV���Z�y|���_c�8�~�L�T�y�O��CsT�PA���DрD1���BG@ �"N�&p�f�mQp�1�Մ�xF��d"oP6M�F	���Hu-��+(��{�a,���G��a�%�G'B*�Ma���v�� t�¼�2��a�N�mZ�h��!b��T�}Q����hWwI���. ���q#q�7�R�V��@|�Ft? Q2{?q�w"G	�=�>���p�i5�7��>�m�dĔ�5�g�E�3P�O�H�l^f���D���pT;���V�à���O,��E�q���7A�5Y�u#��s�h!g���F�S�~CfH�ASN�����zB{jݬE�Jց�'	5��� j�t���6(�f��w�ʕ�X1���W7������@�Ku��q�:#�lK���qf��ud��͋t)���')��e3����ލ�La��7�Ĵ�]21�!�Y�g�vd��N#݂����d��V���CE6 G
#	*��:\�
Q��@܍��v�ͩڰ�b[���6.]����~�<,f��U��h�ۦ�$M�d�4��=,���@�t�n��@�]G�����H�˶k�Ԕ,�TJ0��'(,>��EG5��0/a@��k{}�sKp�?� �P�YE�S�[{҅#7C��iڪo���2�$���}��sTQ1���D{L�3k��w0���0<O�:%["ی[z��F5y�mm,UF��X�!�q��:X� VZ����:��P����>�ԲA�<�kވ5i�A��d�h��7�_����3���,��#U#�{,��QAΆ�;���V"��xX�7o���Z�Ǎ��g<��8`��=�P����(`�g��_\���^(L�T{1y6��\{hz&[:G���Z5�^�u��Ǜ�錆�����r+��Z���5�Y�d��ǎ<Z
�.}�;�Lҏ>"/`��'#�`?:Z�Qv�?�|W��t�Xɱ�Ӳ�[�^CN�r���V�mQ9�m���m�����m]S��M� �l�$��A�!N�EQ�Me:���l�e��0i�C��˨S������@�Ǆ��P��J������a*�,T�8���d�b#?RB�gEca����F�HX٧�H�{�l�&i��!lB�AZ�.�ˎ�c�Z޸'��@�Џ�˫u|�7 ��a!�J�s�4O ���V6`S�KҦ��t�5�-��p�O;P9�]���8�[PK6�rڶ��}���C��Z+rA��I�ڎ�-R���v��&��
��"x 0p1�;m�@�;>�T���ݘfD��[i��_��.�J:���]$L��d�Oy۹"c�
�
�]dh�޴���yl�C��%�� !I�Z���eQ�Y��͛=��jddsJ�N�5El�l<�+	��q*w�&������ږ#�du�*�s:�J������m������ �g��o���Rj�0V#���֍�&A\P�l�	����؜�|60Y4(�i��e�7R��x[��B?��6����Q�K��4K�6ӫ�ֈA�:K,<�lBX���=:��x�B`�|�J�d����{��6��(:��/$��>�S�n���C���*)��b��Mq�4)���=�7��*��SU�M�A瓒��pp�	"���Rļi�dT��Ƚ+a�ށ�Fo^%NY*j�/Z�eS����qJ�a��L�	�{K����mu��νpc���u�K�v:� 	=��xK� �ϼV_�qAc�1:@���d+���ILSX���5�%��.�	y�����:�a�����V��M/�B���;��n/l)T_�/�'
��t�Aok��lM�-���&�+�7�����:�
�$ ��5*&W�hȴ#�4V���9V��l���%��l|�t��w�!��Cv���F�YK6�c�H� ���D�!̫"�(�v��:�{O޹3�<%�2���6�� �DÊ�YX�����sL�|��I8x$��@�6AߞJ���TE��ī������D����]�(6��CPe�ɺ1慎a��*1R�a��(�-�ET�g�ŏ�C���`�Ce&o���I���k9�����^�^����j��?��%~S���rɇ�O� ���k:�_T����۫���r=�#vy�C?'���|��������?�]��䳪�z=�.
߇t9]�M����Qi7��gl��7�s�s��f��=�k#��(~�@��^�EC_rH�~��AZʵ��:c��6���-��_E��Z^6��2n^��3:r=,:��2�P�kHI㪋؎ja�dO�Z���E�W`9+�q�����T�g�f�v����S���Z�9� �nfz�O\� 
)�8����tO�o�>ZJԘm�	�Ѭ�N�32���.F?`����FП-Հ�()�OTJ�j�nr�,z���|g����c���;2�k3Ӗ?2q.P�*ۃ}l���e9�䡭2���q��QZ��x�mS�<WT�+��L��<�dzaT�U�	p+�.;U��0Z������dI1����8�«��ކp�D�j:m��!��t�N�(#�0���l꺛z�DJ���!�@����yI��	�0YV���7��۾{ވ��#Bh�U쎇) Fgӻ5�+pzrW��������p%��ø,���*!�m*�h$�{$z�����r��(��E���OI�}��YN�5E�����Ro؈�����+<9)�6�Vᵺ&[�9 a$W��Ө���e�L��-dҨ�Sb��X�m7_^�V_-�S߮�|���񆤏�x��|���r���R�2	��O�����80`K�w:B�E+���s��
�'��h�m�J[nu��܎TqT������}W5e��z��0�TS%�6>�����������Yǀ�(�u�2z���9+	Εl�����Ԁ'�>���F1�l�k#b�w��M��QZ�l/FHԓM������\"��i#�h�)G�a��c��r����eH�x0iհ���'��dܕ�D݊ಗ��.��v7CE�c��1���fky����6��u��Q�C���P�d!��h����������o���R-��nK�
�^��j��Ci��sT��'�ؖ6��i��O��,�D�8��.Z)�q���.��I8"�����W�e;�ɤ�
l�Ȼ�d |(����t�����xP7�m���kQ/A�< �A2�[B�oD+c����vs�2Z�w���d��r�t��U�=�G�6W���4�l�^��%ud��J�r���d�oLIH������-s�I���h�y��GF� {jYXB9�����4o ���q~��å*�`���2��/_(�'�JaЪ#��K�����h_ t+�ɳ37��t�����pS��5�̔qٗ���A�[
�՝��n�T��2u�t?��%�P���=��[N��>3�w���P8��>�˜�F��h�m���Q�r �2�5#�)Ψ���^Q����IP��� � y���ԱW�AIOR;�:�]о�F`:h�T�	>��*�r��^��u����j`��>��,�ͤ�hC�YG�ɒf��ke=�0���u[������    v�c����U7B �9��Ia��[�}�>S��{��4G鼽J?�z 蒌�����~y���˳J����6�d�]A��ѹ��J���sR���eiJ]��qV�sY6�pn��܁���^�(I�3��x}�����㍓I��MpjDs�&W�꘳��W\w����\����tos� z�uP>U �Q�jO8�~d�B��Bj�w�������B���S��ἇ�S�6���10xb��٣��/�YQ���uF��o�h�-�� �cA��_5v�u0�St	oɖݐAo�fe��@��g����n(����KX.J�Eێ�/��� |�%���F��6��>��
@0Tn�m��e�>���A��HD"z�x\��{ ��,���no�.T�)�#�pI7 X��Fs�2* uƝ�bz$מ¼I��߇���5�Z;i�^��(����*J�@+�	ƀf�}y�ՅϦa?B�����f)(�H�#S_�����y2�EP1��ʰPN)�U�Q��C7�%��h��7}�/2��������M�`�.-T�T^�U��	��J�����$�3�@F m�|��k4� \�Uy�J�����倡��JQ����-#x}���y����(_Y%Aw�,�����&!�cѭ±���r���J�(M��e��v�D�/}��sLAeT9��;1%��3;6��>к#��Bζ��$���a��e�hMl�@h��2�HT��|0�#cj���6,�S��Y��������;�T�L{�N)�a:��Hz� ��fj��}��o�L���.?E�c6_*��� �9�l]Ս�mo��	.�o]�r=��d|ܴ����(�F'��M�ae��^F�]q�IE��/P���Y��{�q��)�����Ҵ:u4���!�	{�7����{�t4We5	 �'� Y��j���H����]o�z͈C�)�������V3SL6�+���A���Ҷ%���Q�Q�~7��b�:��m��� �Հ��d�/��2�dЉ�נ��4
|�5rf����l=��^��0�;�
,0�g�Of�rxh�[#���I�LF�}e(aa[j���YjÅE��A$�hn�pS��m��@�թڍ[S�ѵ�G8C-I��Z��J��4Ê�P1ې��#����Is�=��}�`�1�G�+׏���~dU7�O�0���݇��9dzxvV��]���<�T{X�)C��:t]� �c'��Pr����U�����I6�ن�eI�{:We�K�����W��E���O]�4A���7쑅y���iJτ����@� ��2\�`c��Xb�I�6QNGs���`oF
��!�ԋ
�2��}�`�;3w�!x���Eq�a��L#@V�,_���S,�E*#7ճ���3���_�!M��a���A<l@���^�4��h/��Xji�#,]@mUV�7D���y��/E��i�5���>Ǔ��4w�ơ���u��ѷK�nɖu<��Ezi�G��֯�E!�T�d��uۑ��Bm�$3$��X�t*�^���:��4�}����?;��t4��s�X�	�Ì�]��P���?��tW�	T(��$��gޝl�J��@j�.�:j�5$(����iE^P�i�"�&+�np��A��WdcQ�|C�_\j)�������AB�d��t�����ԁ�m��Z��G���$Y�]�[`���G�,a���K ��u�F>���݈V�� w�b�c�I����9Ɔ �ˉ�$z���&2�m�k��#���Q�w�!�F�+@�Zj�)[����d7�#�:�d���XS!���Gwu��*M��6X�m�-*��D`4N,�칽)4���Q�0��9�#�����t�hw�D|h^������NU�w8��M �1�@�����ЏÙ�K���&�0�p��׭$> bt�<'[�\��#�Y�9[(��Sߤ����?��aT�e�W�*���c⟖��5T"����� �&��t)Q��ۂՠ�>[�*�8�.�����C*�^fXHb����X������HC�s�c[��Xvc[��1����3
^�>UE[*����N:W-�D+f���w�a���E}�t:��ZC�)|ĝ}H�.���W
�������/!�C~��}��C�3�'��k���/��K/^��pu�P�/�ө�'ٝ���_�����/�z��|�d��o�c��G41p1}��J&Pg,\#]��zDp��;��ڦ�����PGV2K��b�a#����2|#��J�}�sgr��>Ź�J��6x�{�t������e�v��<��g�~�ńA	�]�� >H��Ahe�`l��Ȋ*�j!\��1�G�:��7p*=�g���q�H.������2AV�Y��!~{Î��3�3�=ĩ����@a�i7^ �Zy�aaT�cU�Vڽ����F��pC�M�;=u_*�d��8CS�ʖ���L}l���|%@�O�3BC2�d��r�m$7����9���LȤ��b��K�\�?k&+��v@>�j�W�(ǖ����~�����$��{������%ٳ�$
��&k_u��S�����Rf��3�]����}��ơ c�0���������^[)�W'�+����%�a�-ح"g�jw��4,	��-��>	ܙ�����'W���ť�U.�X�m���l��sk]�t�QQ�3�$��|n�!�.+M�I.F V�wVo
N�h��,B��6�S?��dm�'S�[XD��]�MR0;�nǤ�?�v#V�������C�M���t�U䢉&rH�I��ʸ�fV�z0��e~�S@��a.��t���*r9� �H��D�x�ٺ1
|%6�Q`U�BOs�=;4 <�ә���LD������%�' �m�`;Ī��j����ͦ �ӍT!)W����ڂ�,2A�{Aj�4qh ��h�~�Ǐs?��6�yɶ�	�#��͝Yrc�������d`�Z�EK�_B痠ȃH���p���W�D���	Oe�s������Tzd�Z���`��,�^i9a׆��43L�6����Y��B	���H�Q�0
�Ϥ���E�M<�  5.��8Bj�ګv4��f~*X_Uݥ��M=O��,�)}�c)4
��ڧ���_4�4Y�[���h�T�V��B�I�M]�K�W�X�K��!�3Ž2�	�A�>x��)�M�E?�2nQڡK�$����-��j:q�0�`*Ni�!�ԛ�OL}{*�n ^-��"	ګI}t�6i,�Easev��,��R?���Š� �PU�l�k-z	]5�����dr����@�xK�q.�ʽ����Q����	��7��:�4���Q�4��*� ����EYJ�>&�<lϽ��k��Q�H���|mC�)��X�޷����Z�Ԇ�������E<�Za��ȒCU[����{�:T��)`6��j��b4A����!��m�EZ�(Y!+?�"�Ua��z"��B��	!D9�6d�\����o�p�;@��r���Ir[֕|=�⺾SѤ^�+QD����z?SvL�I��7Z�_��y�*_�UT��O�;�ɘh �l����-�܊؀�hK��ݢWK�i�4�y�[Ǵ��]��O.�"x=S�
f�}C�����[��Ʌ?��ǋ��	X]���a��3�V^:���V��%Wjm J���k�������+�U@4J��F�u��I��MR~0�$�ߏ�k�De����2���A�H)ȶ�<���9��<�^]�^���	<_Yw�(ӡ
�B8?�ds����ՠ�Zs_z%:�L৴6w�^e�=���uJ�)aNSTVUc�`&f�٨P�}�)#�[���8�5�*p�j)��DW�u�!!:q��ۑ��O��� ��0���^v
-�Ay�K�.-�.Z�)A�cZ���Ɗ��F !�,�Ԯ^]];�MN��U ���i�4�oS_���|"��A30'(5ΎgA�Q�9Us�h,E�B��7	�	���12    |5 �]���9��8w\"���-��8���~�A)��@�t���*C����@�/�o�:xA��G�aՍ4'���L$����� RC��-A��
ͮb���6>,�f��]�ziG~�jt: ~H/e�#BD�]1oD��`xAA]k=����z����e��:g@�0���%�\��Žļ�����)*�`�a㕧�"Y:��E�����Q�2�Pں>�T�xŠ��A$�=R�#)JnYɴV�E&��-�K���ÿ�r[sQ��h�y�eӼ"ή(�00W�� q@	��í#����R��;Ԣ��v�AcxL���G>���A��[��X����C1w�&VM�0��X0�&a�O�գ6U���ƽe���P������ݐ��y����{!��A�f�ǴJ.��4�:C��
��ޜ�g��2bv� j�b [�Q�>#U��2�x��V_�43��U��wR�(���2�!��nI.!�ʶ]�U��ퟎ�%�c7-5��]���M*\������I.�#+{�v�<p�Z�e��75)�z�,�a$�^�����}"�hNeH>}W9��e ��?.�� ��{&����y�C�AS�;��S�Um"���?���d�Vy���ƚ�{8/���]~U�K����I��T�*^����P���dPfIx /�0Ԉ�'B�B����G��h��~��F_�1TAM Ê͋�ˁ�B��@v5���g�Bc�_��J|�u�3ᵚL��� g��Q�����N�MPl|��V�^�u �����8��I+��$	Ԏ��a����w�Ih<����G�-�zqYy��tM9� �
X���$�Ve�&����O=��$�2(NgD�ZJ��Fkk''Ҕ�	�24�����U�%к����oԽ��n�\z��Cd�}��/�3�.)}���ׇ��-}����/I�}���5]>�<Ag�����/9|�?]���?7y�_��
�z�X>��_�¸}�z�3�w���]~���~���\>�]�M~SI�79��w�?���v�ۜ�`ܦc��߹"tQ�1(mt:\��T���G\����hg���Y�`�.Z��<v���A��J<�CT���Mك�D@�\ы 8�;�A��VI��eV�@c��U�< z�s"?j���;�,�ͱ�~�GM�g��'�q�fh�
,Ny�"R<V����U#8�~5zq�5	AM��$�Z�W�f[��'ka\��FG��+k�S�i��P��Jh$jg�N����� I��囶�R�	�����h�I�8�~��7딡H�IU#u�m\���H�e�|�O�
����q�[@�@��F��q,z� ���cV6K2�s�V������k4�����r�����30�|1��1��a-B��L�h�YO5פV�ؓԼ����$X��w�p��$3&O�r�{�	C ��&�c�1���a�^r`�Ē�&���(�VTR��&�4�o�EU5j5��K0�G���`�4k��_f���#_�Y�8c�M�fq�h�ZF 2�5ܵ���`�I�ġ����V;�v�'a��u?��	N�]%pyg=+�̡ur�Z@�#�g��ṹZ���g���$��*@m�t�����Va�ҔH�Sb��@P7e���,X��Jf�a��a�n��w�͟��=��Ŏ�KI#�kt$76�$@_�������_�8�2	6��i�l㑽�h���R�|�V �,�<o��P
@�Ne:%����n�=u;��qO�9��![m�~�<�s���uG��sA�Ttmܜ*96�*6�⫚���lqS�+�PO�p�!�ט|GF���M5��^�o�QlW�E@vX�	ċ�L��Ȍ��RBl�,HQ�,��h�1Y.H-e��$B���XGQ����{�^�  t�CU�y$�򵽿t����
8C�B�G��������8�0f"3Bͳ_�V�S���s6䑈2,£O;�+lzN�
b$��^�|��Ú�V�,�TB����e\�86Dm�QT[�:�}y@ح�aX^ǨR1By���o�{ݫ�K������T�Q8+Hi��j�rbr{�b���wY2���X�Wk�d���t%�)�i~�$4���պ� n̫`��y��s^���@W�tB�6CM���H4Au;L&�;��vE�1k�3�*�R�����x���q�(���}L+�ă�f@���t�����gf���b���Mz���w�жr��
i̻�rt��`M��D��C��_�3����RB
_��!=�%HL��I���}H<��,t�����n��Y>�%}߾����?�������f~P��h�ޟ4�h�ܗ��A+��wU:ih�:-�S���qC�`�Y�~�C�!�`���	�����I�R��R�(� �!�Â�l c�ߍ��5J? � xQ|�Iy�b�Y�F������'z�4��k��+���6�*�z�uY���/0z 9$�[Q�l�:��J�-�8d�Ίy7�WV� �%��!�<�n� ���'�(�u�bc�]��h�+��Ft6#Ά��/�0-9O��V&��}!�[7��m�XC�@��8��j��Q�5W*���� ��x7�$�����A"p����I�Q9��������07U���GK󃨎\����2�X(̱��+?70\hЈ�+05]�d0i y;��������'�e�C`Ӵۭ
��!��H՚{6 ��;�ؓ��J�ANj�����֫W�4`�QG�+�ճ�#Xʤq�W�*�Nݰ� ��)C��u�)�z�ņ����QR�0F�1Y2�jV[,A�6����n��J�F�� 2��v���z��I�`;/n��f=ߌ������x����#I�o��n�GQ���Ѭ��t!�	ç�+٭���^�]v5�a��PO-���v�/P�HzE`��2�$V��3*�d70Q��n��1U�u�( ���'2|�5Iu[���bPq��w�Dx�{q�WU�}�3j�c!J^�wF8/���B�;�D���E4��ͨ�+����ϯrc�~�U�����v��a63�n-��E��0�G�� `��u�T�+���Y�1Ksi'�Я������)(�2�83�v�$�����g�%K�����D�(:<4��e�F*��,�B��8��zUY0>�u��d9nH0��5�jh;_��=��Oq���`V�<#gH�,�T��3yo�Ʈ���b_�H p4)f)�+<P����#*��J���`�(g[1d�N	�o��"dk3�K~�Eʃ�VQX`���;�����^���hs�ց���y:���G.r�:/�G�
K�dz�/�n/�'� Y��{���)W]�˳=��ݱ�M�\])o�iClF��]F��J<m�Q��wP:���΁: �Kt)�tIKB���kӨ�8���`�3mDq�E�	�1b�{����!bu��(�ՈJ*~�3�$��ڸO���/�A��� }�f���N�����W9 ��*����6���I�6�b��&�{�2�����
�&T
UX�D����i19!�֓��|:�I5�uВ�|��$߶�����T�~.��J]��;?���+���U�n��ٛ��9r�C�a�\i]u�H����e�&���O���H��g�XK`��K�6���:ai����D>��	��|@�&r��H��[�����l��uv;,�|�!�8H�j�(ȩ&;�����/�~D�
r�.��[Fj�}���
	�ӗV2i��]l�00t���/E�]�jTry��#E<��Y/�ʴ]���䴇��4��Xy�.B��#b?sna-���޿|t�����b?�O��4\�T:�'���/w1ybߌ�C�m<��3�G�I����RJ��5�A7�ne���������!׉�֯2���*�R����%�*x�Z�0�l����\p$�4	m-=��J�^vn����j�攆���w�YZ ���'Ⴊ�e0 �?'�h�5��[��2������9�Δ��b���;R�av�{4�8fDLwӪ:V�~[��z���4���ڎ������i���h%�z\�w�h��A�86����O����J��sy��p� oJ4���1�    ��\M�lOF��f�y`��W�Ƌp��C��աrks+BPD(#8�\�DX ���h}. �d��IU%i"=���M̀�3o��DpH��-��YyxY�o�bu�^���{�|"a4���(�H���CNT.��Z�ٜ�	��*�{A��fXԵi�ʓG/���ݭbc7�D(���a���>[����@��|Hqs�V�K�_���YOK�j���v���'�K���"����U?�G���a=���g�l�r�i$�]��ɯ{��t7	~���:g>ش����t~G�w����`ˏ��/j���E�����%DE�C�|T��T�{|���,����\r�JD�\��k�+�W���]�[T�Aq(�
�K�d>�^B[^j+�`�3����X��1�!:���|
']:^Ik�3�Z͗��kaYn�R��D��AQ%����m�Am�3î�뺢���~OX�I\�'~��LF@X�#� ��4|j��HM���a��6�u �{���mG�K�Q�s9��)��Z#J�޽Rٕ�'k�A��&cA�r?����B����R��9�q��eWA�ũ�Q �[tx�!���"��SO�F{�/�O��A�H~\�[N���/�G��k��7�}�[�i���{�Y�zp�f�I4MuY�pڑ�~�=������eҺG������U-]�R%<Y筁N�/Kc ѳ���0�)���@�xt�}_�?�MFct�%���<C��ʶ� ˡ�D�s3<'̝	�C���p��Wy.�9
/�^��Ԭ�v�`Xޝ�UL+sV����שZcLL��[��`(��jT՝�9�`/��^��@!^(�uu����C������k+�ALz4A�[Bv�R���HhoF�R��L�5�W�����띥�RIi��5�R7��X&���d��>���\�mju,K��d�+u��s	x�W�&��X(�,�R��0k�$��:��2.��P�z%��w�%��#������n�9΃YCD����� �̦�H����Ŕ6J����Q��j>"$"� ��&V\�RtNi�_��{����{��~E���g� Y>	�N�CVmNўc��&t"zǃF�muȥ)���i�� �V$� E�e��2}"F(���(l��έ�s�m�c*W��8�WJ��/�(i	�3���U��=m �o$3�N��&��Q�\�}�80��T� +�%XB�wn�5e�w�鈡ʃ�T5�R�r/�ߗ��I��v�ou�z&�!��D��~p�?��}5�1F�8|�%��q�!���.��|�V�!���*��Q�Q8L"'(Ɂ���eRʤpW6���5f����"B�����v�`^T�;wF,+�BYư|�F�A�7�zl��ѐ@XAZ����`<��(�uM̻��dbn%�C��]���4E��SKv�L|��M���^I��ªܪz�X�I���h�W� T�r�m�֚lWH�(6%�)F��	��_>�Ӑ.W��@�مI���	"RÆb���2�&"�`߲��8&cb$�3��!����K�V}9�oMy��>	���{BY*<��$�i�Ջ�|'Q�n���=��2��?�t��S�3���X����h��$$$
+u��-ySr+�T��c��k�]WcT  ���9b�4��pc� Lk	>��}юgT?٫��,LBz�ci�F�����I[8�L����E�u;DDt�0*T��N�4sG�١ٔ�[��#B���~"��)� y�du�;iv���
5������d|+���C�}Hh��
�z���ɟG0�d�JBU��:soh=1s��l\���:����Q�����,u��ҹ�0k��ާѪJ��Vg�s8�tELv���q��d6�S��&�\��v*�R](�Լl�(��Z�է��X�T�u�5��%���`��w��$�9J
N6+i�`�¤%T�N�����@��E�i��]	�]�rp�8��DN�EQ�!j����;�
�
��ӂ˕A������!8�&
�>V�H�J�q$��g2���sW�j�=����3��5W�؈yi{�1���xr#��6�� �H���ͺ�����܆X����B`"��̠�9�/���yL½u�>��"1)<��I�'2�b��`l7ǡ4�N�����{,�J��a:q��v�@~��;��@���P�!e ���s<�{ ���bUdD����@[�]	�1ÙW���1.Tj)�՘��"�X��Y�λӜ?s�xGe��;��;Pe�*8 ��r�W��Y3���x�˂3<&��B��S���Jߑ����)�͉!��'�6��� �����AiA�ߖr��-H��2�s�ء�eTY�Q���|�[j��R$M{$�<��F]�)3���v��P�a�w2aA5�YR��l����^(�P�RS��j�&|>*GR��y�S�ÂY#�kv'����O�e&�d��~�p��=�@���X\~7�h�{\U,5�P�5����-�����P}	�G�5a���/�ư�#Yߑ3�b�Y�e�\�fF���1��m�䷭`UhOj��
0Ѩ��t��W�xz��3Nۡ��}�6N^��J�㧇�I4�Ċٛ(1�gV��y$�/56?�N�z1�`�Ȁ�_���M!�U=���_��tl��.}ߓP
���[���9�ta,n��@�z�9��L��ϱQMacLa	��z�*���2�k�ycљ��>]|�����7h>�Lg9����I�gex��Rw��Te0����
��g�ĥ"3�BP4�9���� �}��a��X�b����s
i��TC������ic�ȫ��F��h\�Bm��WE��͙%3�	*���� �%��f���C��.��S�r#b�K,P��@��h��-b:.��Y��լɯ�>�W�Q/��`HCόc1�'w�@���׉Z���5^L*<�O��E���B��]�&c�|�W����kG���	RV��v�n؜IW����ͣ�W8T�e��$������1TW��^�o<�`T�f�w�h-��gZ�fM`"hZ"(܀����b���u��1*�a�2ӿ�ϻ�t��EN2\���.�t/`g��@�(�JI�mW�ԃ�3�� �Vi"?��c� C�
R�ݕ�I^|'�`ڤ �����bU�a�2{ۡ��FH�.EQ���O3=�J�ہ1��(�j�܇�*�(v;pH��	.���N�qho�Tyk{�d=W�q�+?�3!�{���Gn��50s��%�4~\�\�h����˭��y����s��|�0�j)3���o=^�-}��?>�|��)�����._7�4䝋|�v������-�0sg~�_0s-|�����������H�t�C��'}����3l��e�K}��Tp ��������aZ�H�nty�}�n�u��l�:�G�7�u�8������+���o�
��XT[zH��L���ƨxY*��}o������Y�W�]�+�Dj�~%	��*	#ZMy���ο[��o���&��J��ѹ%�p��YW[aS�Z�K~I�F�ة���v��������1�Ew��If��?����9<������˓���	Ge�~� �؞F���v��T��#� �C/P��)#�EC����CL|���_ܠT���_�j"��	B~ȂF����#{�S��*8y�k"�>���q�(W�GNI���c�0*���C˾�zu�����h! �9{�`��?o�^��R�^� ~8��H9Fr��C*�C���vb,ezU��0t)�2,�ѣ������xU�RÈF8�R�(?��Vĭ~6�x����m�b��J�E�6��d��fu�%L�M�ꫪS�_|�2�q�G�)�n�0�b�#o���vz���K�q*�u0� 3зȶWv��S0}�4H����dJ��1��s��]�F4
�DA�$��NJ�#���k��:���2h�H���ύ��M���01 �5O���.�.{��wn:eFǘt@�r!���    �6 CE/}�L�f�Km����d�@HH�2���A�7x&L"�T�V����5����� �@�y,�[���P7�W���=ׯ��2c�������r%�Wy|�T�>��	����?���C�q��3� 9^yG�(%�P��]cI��e�k4�z�n���6�(�M�aI�َС�L8Խ,G����t�O�n�y�j���:��c#<)6���0��d�������DM���#g	j�K;�0�=��@�f�`
If��x�U#�>]u�5����୽K��
�ʰexC�9�E8���p�*[�����n�qwp�>����g�$5GmG@@N�=��F(/g/Q��R�iɱ]R4�m[��!l�&d\��m����Z#�{f�����L���Ǳ�x{ P[�������j�x�J{n(��Ak�A�{�<v�J�q22�pMP�=�K߁f�P�bX1Ԣ��^`��a�r�Y]���1��߂�K-*��^in��%�u�(�ʟ5G�,#�9&�����F�Qu��!/�"'�GL�_�|Z���r/PD4�.�;�)H��·��A\	�H��zC�x�K�5�鞦1S��A����^���� 38�]�f�b""1�GH㥵��$���W���C��s�wk�RB����e�MK�D�kU�zÖ��T����H�W���A���Ш�k�M;�n�I���z؁� �����H)�Z(O,W�&�d��Rr�/�J�f?p��Dd*�MT!H �y�>ԫ^�����I~�i;�^��� �eO	ٺ�Ǌ��P���+�rl���]R�ܰ���1���I��ȏ+�� F�u����vT�S<%HzY����a�U��T(�@2{��"d'�WH�W ��!/i����g��h����%*�grw̘�Ek,�;6Z4���c������������}��љ��X�ڀ�W�j�;�K=�;	]�ݦ�(�א�C[9�`�@|����b��*��,c1�:���JW%���
FfU�,7�>(;�Z*Bg�����Sh(z�b�����\���n_���>?j+`�:����iP�%����4������ZZq�{�6L?��d���,���b}����N7��-h�"������8T}%���1pv��Ώ;�.H�\<��|�T�Q-��ţ�F���M�)1�TD�|[wP��A'^�DT�+Q���ޏ�n$ȹ,s�]��� �bxMb����t ����B&�$�A����5�BP!B�U1���t)X��eρՅ���*�k�Mo~�_�DH#��w��B��Ow�D
�z�K!�b�����s9>��%�A,�<T��+#u��&?��u���S�,�������ƾ�PD:�Q�T��l`�{5xv���S�&��ꂔ��B��>�1n�
�F
$$��B��&-g�p��U��B*!������r�T�Ӗ�/�Ћ
�kG��A���<����b�1�M���F��3K��
�fqN�ƨ�l��@/�Q��Xn�ה7/Iߙ���ׄCT1=jW�tДn, �o�5�v`��aR��k X���qI!>�ְ�g�f��o�Ǝ������8+m�JM+�W$k#Hb�N`���E;���)n@U�'��6V&5Jy�61��*��E�l7h)P=hl`�&K�ҋ��?~�[${��χ!�S��Q�$�wU3���to�6!ߤ�sIa���� 9�fm����>oH��5�.eD��a�Թ1y��(6 DI"�rP�d}��*S���U�W}[r��B��TsS�׼���nʮo�5H�<R��2��2GLW�Ҧ��\+�� }����r��W�$��F-Ę ۉ��J��n9Ƅ�ժ3�<z�ߏ���J
TU������t:�{**��40�fG���R�{d�`�F�C�D��@�� �E�F)��S�6ܭ����(�<�ʠ��K8Jc�S��ְ�yQ%غ��|4k�ˡI�F�����@��k��Ϝ_��#Ӓ!Dz��^���*�m�@��'�Q�d�J�9}1�'r�h\K�3�M[z�eA�6�<�H����"��ŨX�W&� ��U�c�2dJ��׋��ݻ;+�b<�-�y����?D�_��H�|��BU
Xr�r��7��|�[ݒ` ��?%@�2;��jP��sl���M�B/�B�b
ؑ��] �a,��4�z�e�B{q�Sns$�?g�f���~\�צ�z�?��fY���:K����.�"��)pe��#H��ȋ��I� W�ҿ��4X��
��!I�Ƶ���O�)�2��{{
��:D�u���MoEe�Y�WtK7����@���6��N�ul`s�����P�0�X����0�I	��j��:�C��)ެ��&ѿ�*� �BRۑAP�O�C��@R�\�eq0�)������Fc�3tuL`��-D���$xe0�=Jp�;��ҧ���B;��b���jB+����76#.@�}�al��B��
Q�J�U��$�vi�,J��4�z�@x�J�L�̝�,�j�n-��p�_�E�jD%���ƚn5�_[~l<<)��|�2]���V_�襂����#��g �O�C'�U�e���`u-�*.�������${�p��@�"¿@KXo�CG��H;y�/W�_k)@���!0�j��MZ"���|y�y��:?�B�,5�MO��J�`>��,3���IBCV���q�kB�����Vi�H $���������s�r ȑ%��͙;%w:x��e��0�t�����AA��X}��<�!��K#����R$6��lc��G��%����C ����c���3c��<��7�	:���0�NhҰ��s�o�P�|�%�<��`� �Y��P<h���r������3��&�N1�	��a��_4��f�	^�y�:��Ɔ0Zg���Fh*Ov���Ry�TT�i_U[p#0��9��`U��LmM�G��b��y���r_� �\�v%��)R��S�� r2r�+~<�6�Zħt�Doȉ�3DU�H/�jjT�BY
q���
:{�V�J��sJ���agS��Щ$
��[?<��JM�H1��hH�G
��� �X�enF�!�9�����g�4y�
���F�<N1n�kz��X�d��V	�V����<,tm�F
Pe�j�Q����t �>(�I�v��a�1��-�Ҡ�Qt�2���X�X���z�n6(�>�����5���|�|"��	�B����Z�t
�Y� w.�@�Q����q�:��EI� �IR/^+����������(�u���*����
Q-78�x��	���<��z�����^��+�:x�V+�F�n�Q7��:�O@�(u�GDu7��6�������16��ڠ^qR���ZT�25#�Y �9��];]�2]֕�����E�¤�6,������$�F����f�"y'��y��R�Y���R����l�����MA�IBk��y�.e��f]�QX�s��j٫ɏ�LW��]L��-	�>��%��n�x����T��6'BP�/Vc���wV���������P�5E�b�g9���+���	r��k|9Y���ӌ����<4r��!'�B�Ju��.>"#�l@~{�}@�4{ۨ�J&�H{)����Y��s���P&76t����9�֘�LF��p�Dp9!Q��k�m����MzU2��=��c�^�Ļv{|EX�.H"xB���a�9�T�ɬ�����b,/,#"����r�䍪{pVↆ8�.\5V�j.X�E߫j��):(��2Iz��GN�2��t47Eϳ (�;Q+��Ln����������Q�fZ���{a!�P����,���� �=ʛ�0�l& <�A�݅��<�b��3|�p�����u)�����w��J���'�|�N�^����~|�[�����������.7��?SC����<���۞�`/���o�����o�-�QO˭��d�Vgg��.I���P�̽�ڇu�Ԫ@��E��|@���*�T.�V��� c  @�+Q}7]�W��H���� �q���/B����I/$Ij�,M���r���0x�{  2]]'p"iN-1Y{��T3�\J��0��7�� ��ҨvRP��jY����M 	�����7�����9��CMpb��(BAu���Qn�=#�j �'p���\X�f��P(�%�F�i�3�=j��[V�!��Y�ZxQ����[H���3�/q
cy4�T���̄�����S� Dt"��~�pЎT[l��ǎv���k��Bu��C�g�����O/Ht�C4�l���avS�����Z��i:�2�ߗ�t�k9���J3f��f����+F��*�G��]�
�O,^�4vV\��e�UI�2��fN����`}��e��R��!� �`� ��e�ơ��P�'������*a�R���p��OP��:�0�����`eվ@�4iK�U�<��s	okZc����H���7Y҄t�x��!P"�ʾ�+�N��@���Y�#i��І�ض��1�<V1M�5H�P`*�,�����#��"�3br�w�Vӄӂ\��)&tcufV脖È���$RV�H^ 3!�2�/�+�8�Ύ�e��'|��(�pO�ޚ_�����u��o�bzSa�$\J�{��Kj��̔��b� K(��u�B�q�$?�Ayi�����8TEV�Ԩ�z*��C��묒!z!4�è} ��a��s33E�$Pn���ei(2<�a����eF9���N3�t#.v����7����:�+T�Ƿ����ťxs=�΍u2�����L�b��KK;MHX��&!�gg�*@<� ]�$_ �@;w�^�@^�e]e�q]��1"���i������D~��
����*��a�T�<T�l8�؍�^v��+bKQ�65q��h��$
��X^q��[$z�{꭛�n�wb�QpD:��Rlņn��������x@�����zQ�eqy##����+v�7��N	���Q8���`�+5��l�_���{OH���/��3Rܘ��F������X�5D�At.��c҉؛�"3��+JS�X��%�UTE��T�b7M�t����1L��������P�      �      x������ � �      �      x������ � �      �   �  x�ŕ݊7ǯ5O1/p��o�p�B�6�즥(Gi3����)��O���D�ŪY;����!�Kh�s~��י(L�CpВ��l��0I��9٠xp�����^Ъ�l�����㧡��a3��/��iQr�Q����M����r���`�k�1�:e-2p(�"�$rIJ9[ø�8�XԪL-�5(�[�H�=�6�&!���Եc��c,3�Bj�F5|&�Q�#*�t��(i��kyH\�'�j�&D��n�_�}Ώ���5��3)��RBY�FB6��y�'��p���dLn����������}��B��_T�c?.CG��}�5���l��EEɡ ��xn��$�� Az�3R˕��r�����EG;�Jq�Z��w�%�z�ylS�i�$,���A���]�vu���R�b �ͷ�ˏq��"W���)�� �bTNXI��}��H�is=YWθl��Ή���yA%J$NQ�F��5R�ȶ�-���=��)������W��9[X;%��y��T�'�-�U͋�8S��%�U�E.OTk#(S��-DU�$W�̡��Ў�gq}��Vۇ����P)��s.��Sz�L�S��b�z�'̤ڙv�u�*Q��i�d����GVC�?�K��6y��bխ'��k�)!��~0�K�4Ď֩OqC�PѠ�ܟ��5�ę}q^�죟��IJ�3imQq]�e���R=���P@�KdPQ��8��[v�v�e�|H�n�}Y��}Qu5���+���ka��b��<��<O�P.l���i�8.��y��md�(U���q�Y��2f�{~`-�SX��Oq?�?�T�i�}E��X'���%,�"�yr_E�BY@Ys3��0o���T�&ݒ��ԃ�J@�z��j鱵�p�����_�����?���ö�6�������7�ϟ���em�Y���ݗ@s��>��?��8���*_X�HY.���6UU��]��      �   �
  x��Y]o�H}v~�G#��N5�i�Z-QȰa	 `@�BB���8tۍ݆!���y��վ�[�؞rwBf��v��h�]��u���k(TQ;iX�bږ�U�"F�<ׅ�2�lI����U7��iD��5��q�dI�b�e��}���������jJ%Je*)�*+�	��Ȅr��J;VWQ�@U���"�,/��uYq_1�k���`.Y$�t%K�Hf������J`Aa�V�WZ2�uU�Z�6�̒�t���H�Ded��B��8���Lr���W�(��̹��]dM{�&���s�*e,5#-�FZV׵eF��@���ك�����E7d#o��fg��{JT��k�??:t�G�m��%�7[0!��Y��H�U���zfK��*�e�|xv�^����;��ބ5\h�o���f�����L�hI�]K�d�G�o<����.��,	���N����U�#z�
'�q�o�y����и.���u�b�Ͳ2�(��LZ��.���bVY]r� �igt0�`W �c��c��I^+%y-�|� ʹ�>r&��JfG�>͏�źY���B�wn\�6�?���������ǿ��^V
РP�T��F ��{΅���L)X-�g��uD������Aٓ~5eW�^M7�'��?�R�2)`��j����7P�pX�ĺ�W}��`��n��������1��X���v����ٚ[Y��(��*��Qq]�\�"�����MKٽ�_�<�ߵ��<���N�%��p�ic�[�z�^�e-�.~:?z|v�6C���)v#�-'u���v\,��S
a8v��ckUe4�h�MZ#��˹A��a�� r�^t'��]{>x�-��[83��LJk0��uv�䊇��]n��4�|xs~���ڙe�c��_&�Q��s)f�BfVc׼�d]qi���K�hlJU�ı�
����!Wf?cB�R����R���}��T���M1�%��b��̵��JT��&����A��jŢ���?Thb��E��1�B����Qv؃:�;COC�Y��]ek��M��}�y!j8���5�ͦt�W��j!
Ҧ���:M�m	=%^��R�s#�s1�r.��,��2Ո��"_%�tP^�P��4VC�Y��$���~Ky��J�f�.���I?��w�oP����߃UBUF	 p;Ċ� ���׆�,��a�HUUĔ��� ӕ�\�}���Ǚ����xTY�PHw�"�b.��� k�C��[6Ú`��@)ƌ���Jاk��F*US�<{@H���C�B��؜gg�V���J�������ю��-��V)��s��BV^�22{ظTq�����~t�0'����!�P���t�B'=� h:j�*n��B��"��62{
�W\��/Ū��8�����v�����Ν��2���.�!��h*)�����}��;�7������TPh|\����Qx6仵�*Ǎ���H� "��੣r
s��������4P���G��u��"�Z�T��Xy��	DRR4S�j_&p�ȍ��p���Ӈ��e���{�b�a�XнK��7}�@0	�w/?���������E*��
Z��u(�-�K]�B��Sr���Qe�|w���ᣣç�S��:���d:G`%�Q�R���<d~�6��l�*�Y����Ĳ�fG3�]�&It	��RDMhpUj��!��Pp��P/A�@^o�:Q]� (�m��+������p*�(9���:����L�y�!|v�#����	-�]�pcEz�k`������AK����v�B}Z���?�O���7h۳�CN��F������lMR�uO5�u���8�]�|h�r��q���I�s.�"o��'�[QOT��[���pZp�a��j�AO�ګ�����B���%	Aó>}e����<���ͻ.�w��r�LzD��s�A�����e��X�w�C��O/�>����a��C�v��oǐΰl�ȵ�LX@��,$��jCR�4�t�	��y�<1{վj��������)y'#���F�.��y ^|D^I��n����|z�0=B��c��ݸc�]���N�S���/?L�r�i�M���d�������ݴȺ?�4��!C�5�*��_�\:r���}~J�{�6LFƱ�ʋCX�}�Ώ-V���PJ�hڷc�%4^]��H�N��e�v[����'�5��$�������FM�"����:��� o��\��˦5�+lH��p�%��BIn�{_��!��>�3��Ht�RX	5)�n�>|��f������}�{@>�����5�؃,`�%��QQ��q+�����M�ܛ�w����o�i���$����g���5p��~��2�PD�U��lK)\�#1Ls��xr�Y-�%�#x�`������O�̀���y;�0s�[����A����AZ"��������҇<�R��.�Ȓ�t���c,�1i�{TIQ�ED6�1�l%����w��l�<��d? \JC�3DW���V�C��Y��v���,�EϦ��͜�Y�m)��x����{ �6����p�/'Ђ�/�}�2����f�.�"��%�6AjY����4�a�B��Œ�B��7��$Oû���
��/���OϏ��;y�)ԩ�V�ر;F��S*�;~O�D�B�=�pl�[�|��R�?����jV���'3�
煖)d
m���ULz턩Q��7~i�����=!vn���HT`Q���,N8���Be9�Z�/���Ϛ��j����_Ѳ     