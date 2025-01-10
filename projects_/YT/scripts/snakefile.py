rule all:
  input: expand("projects/{project}/results/go_table_{logFC}_{adjPval}.pdf", \
  project=config["project"], logFC=config["logFC"], adjPval=config["adjPval"])
  
rule ontology:
  input: "projects/{project}/views/present_{logFC}_{adjPval}.RDS"
  output: "projects/{project}/results/go_table_{logFC}_{adjPval}.pdf"
  params: 
    ontology=config["ontology"],
    algorithm=config["algorithm"],
    statistic=config["statistic"]
  shell:
      "Rscript -e 'rmarkdown::render(\"projects/{wildcards.project}/scripts/ontology.Rmd\", \
      params = list(ontology = \"{params.ontology}\", \
                    algorithm = \"{params.algorithm}\", \
                    statistic = \"{params.statistic}\", \
                    adjPval  = \"{wildcards.adjPval}\", \
                    logFC    = \"{wildcards.logFC}\"))'"

rule table:
  input:
    mapping = "projects/{project}/views/ens2gene.RDS",
    deg = "projects/{project}/data/" + config["DEG"] + ".rds"
  output: "projects/{project}/views/present_{logFC}_{adjPval}.RDS"
  params: 
    DEG=config["DEG"]
  shell:
      "Rscript -e 'rmarkdown::render(\"projects/{wildcards.project}/scripts/format_table.Rmd\", \
      params = list(DEG     = \"{params.DEG}\", \
                    adjPval = \"{wildcards.adjPval}\", \
                    logFC   = \"{wildcards.logFC}\"))'"

rule symbols:
  input: "projects/{project}"
  output: "projects/{project}/views/ens2gene.RDS"
  params: 
    dataset=config["dataset"],
    symbol=config["symbol"]
  shell:
      "Rscript -e 'rmarkdown::render(\"projects/{wildcards.project}/scripts/mart.Rmd\", \
       params = list(dataset = \"{params.dataset}\", \
                     symbol  = \"{params.symbol}\", \
                     project = \"{wildcards.project}\"))'"


  














#############
# 
# wildcard_constraints:
#   sample="[^_,^.]+"
# 
# rule all:
#   input:
#       expand("../projects/{project}/results/{the_ontology}_{adj_p_val}_{logFC}_{direction}.pdf", 
#           experiment=config["project"], 
#           direction=config["directions"], 
#           the_ontology=config["the_ontology"], 
#           adj_p_val=config["adj_p_val"], 
#           logFC=config["logFC"]),
# 
# rule run_ontology:
#   input:
#       expand("{array_path}/{experiment}/results/{contrast}/{lista}.csv", 
#           array_path=config["array_path"], 
#           lista=config["lista"], 
#           contrast=config["contrast"], 
#           experiment=config["experiment"]),
#       expand("../data/{annotation}_gos_{the_ontology}.RData", 
#           annotation=config["annotation"], 
#           the_ontology=config["the_ontology"])
#   output:
#       "../projects/{experiment}/results/{contrast}/{the_ontology}_{adj_p_val}_{logFC}_{direction}.pdf"
#   params:
#     algorithm     = config["the_algorithm"],
#     statistic     = config["the_statistic"],
#     adj_p_val     = config["adj_p_val"],
#     logFC         = config["logFC"],
#     lista         = config["lista"],
#     array_path    = config["array_path"],
#     annotation    = config["annotation"]
#   shell:
#       "Rscript -e 'rmarkdown::render(\"ontology.Rmd\", \
#        params = list(lista        = \"{params.lista}\", \
#                     experiment    = \"{wildcards.experiment}\", \
#                     contrast      = \"{wildcards.contrast}\", \
#                     array_path    = \"{params.array_path}\", \
#                     annotation    = \"{params.annotation}\", \
#                     the_ontology  = \"{wildcards.the_ontology}\", \
#                     the_algorithm = \"{params.algorithm}\", \
#                     the_statistic = \"{params.statistic}\", \
#                     adj_p_val     = {params.adj_p_val}, \
#                     logFC         = {params.logFC}))'"
# 
# rule select_transcripts:
#   input:
#       expand("{array_path}/{experiment}/results/{contrast}/{lista}.csv", 
#           array_path=config["array_path"], 
#           lista=config["lista"], 
#           contrast=config["contrast"], 
#           experiment=config["experiment"]),
#       expand("../data/{annotation}_gos_{the_ontology}.RData", 
#           annotation=config["annotation"], 
#           the_ontology=config["the_ontology"])
#   output:
#       "../projects/{experiment}/results/{contrast}/{the_ontology}_{adj_p_val}_{logFC}_{direction}.pdf"
#   params:
#     algorithm     = config["the_algorithm"],
#     statistic     = config["the_statistic"],
#     adj_p_val     = config["adj_p_val"],
#     logFC         = config["logFC"],
#     lista         = config["lista"],
#     array_path    = config["array_path"],
#     annotation    = config["annotation"]
#   shell:
#       "Rscript -e 'rmarkdown::render(\"ontology.Rmd\", \
#        params = list(lista        = \"{params.lista}\", \
#                     experiment    = \"{wildcards.experiment}\", \
#                     contrast      = \"{wildcards.contrast}\", \
#                     array_path    = \"{params.array_path}\", \
#                     annotation    = \"{params.annotation}\", \
#                     the_ontology  = \"{wildcards.the_ontology}\", \
#                     the_algorithm = \"{params.algorithm}\", \
#                     the_statistic = \"{params.statistic}\", \
#                     adj_p_val     = {params.adj_p_val}, \
#                     logFC         = {params.logFC}))'"
# 
# rule run_annotation_gos:
#   input:
#       expand("{array_path}/../data/{annotation}", 
#       array_path=config["array_path"], annotation=config["annotation"])
#   output:
#       "../data/{annotation}_gos_{the_ontology}.RData"
#   params:
#       array_path = config["array_path"]
#   shell:
#       "Rscript -e 'rmarkdown::render(\"annotation_gos.Rmd\", \
#        params = list(array_path    = \"{params.array_path}\", \
#                      annotation    = \"{wildcards.annotation}\"))'"
# 
# 
# 
# 



# configfile: "configurations/configuration.yaml"
# 
# wildcard_constraints:
#   sample="[^_,^.]+"
# 
# rule all:
#   input:
#       expand("../projects/{project}/results/{the_ontology}_{adj_p_val}_{logFC}_{direction}.pdf", 
#           experiment=config["project"], 
#           direction=config["directions"], 
#           the_ontology=config["the_ontology"], 
#           adj_p_val=config["adj_p_val"], 
#           logFC=config["logFC"]),
# 
# rule run_ontology:
#   input:
#       expand("{array_path}/{experiment}/results/{contrast}/{lista}.csv", 
#           array_path=config["array_path"], 
#           lista=config["lista"], 
#           contrast=config["contrast"], 
#           experiment=config["experiment"]),
#       expand("../data/{annotation}_gos_{the_ontology}.RData", 
#           annotation=config["annotation"], 
#           the_ontology=config["the_ontology"])
#   output:
#       "../projects/{experiment}/results/{contrast}/{the_ontology}_{adj_p_val}_{logFC}_{direction}.pdf"
#   params:
#     algorithm     = config["the_algorithm"],
#     statistic     = config["the_statistic"],
#     adj_p_val     = config["adj_p_val"],
#     logFC         = config["logFC"],
#     lista         = config["lista"],
#     array_path    = config["array_path"],
#     annotation    = config["annotation"]
#   shell:
#       "Rscript -e 'rmarkdown::render(\"ontology.Rmd\", \
#        params = list(lista        = \"{params.lista}\", \
#                     experiment    = \"{wildcards.experiment}\", \
#                     contrast      = \"{wildcards.contrast}\", \
#                     array_path    = \"{params.array_path}\", \
#                     annotation    = \"{params.annotation}\", \
#                     the_ontology  = \"{wildcards.the_ontology}\", \
#                     the_algorithm = \"{params.algorithm}\", \
#                     the_statistic = \"{params.statistic}\", \
#                     adj_p_val     = {params.adj_p_val}, \
#                     logFC         = {params.logFC}))'"
# 
# rule select_transcripts:
#   input:
#       expand("{array_path}/{experiment}/results/{contrast}/{lista}.csv", 
#           array_path=config["array_path"], 
#           lista=config["lista"], 
#           contrast=config["contrast"], 
#           experiment=config["experiment"]),
#       expand("../data/{annotation}_gos_{the_ontology}.RData", 
#           annotation=config["annotation"], 
#           the_ontology=config["the_ontology"])
#   output:
#       "../projects/{experiment}/results/{contrast}/{the_ontology}_{adj_p_val}_{logFC}_{direction}.pdf"
#   params:
#     algorithm     = config["the_algorithm"],
#     statistic     = config["the_statistic"],
#     adj_p_val     = config["adj_p_val"],
#     logFC         = config["logFC"],
#     lista         = config["lista"],
#     array_path    = config["array_path"],
#     annotation    = config["annotation"]
#   shell:
#       "Rscript -e 'rmarkdown::render(\"ontology.Rmd\", \
#        params = list(lista        = \"{params.lista}\", \
#                     experiment    = \"{wildcards.experiment}\", \
#                     contrast      = \"{wildcards.contrast}\", \
#                     array_path    = \"{params.array_path}\", \
#                     annotation    = \"{params.annotation}\", \
#                     the_ontology  = \"{wildcards.the_ontology}\", \
#                     the_algorithm = \"{params.algorithm}\", \
#                     the_statistic = \"{params.statistic}\", \
#                     adj_p_val     = {params.adj_p_val}, \
#                     logFC         = {params.logFC}))'"
# 
# rule run_annotation_gos:
#   input:
#       expand("{array_path}/../data/{annotation}", 
#       array_path=config["array_path"], annotation=config["annotation"])
#   output:
#       "../data/{annotation}_gos_{the_ontology}.RData"
#   params:
#       array_path = config["array_path"]
#   shell:
#       "Rscript -e 'rmarkdown::render(\"annotation_gos.Rmd\", \
#        params = list(array_path    = \"{params.array_path}\", \
#                      annotation    = \"{wildcards.annotation}\"))'"
