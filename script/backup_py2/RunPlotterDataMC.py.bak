#!/usr/bin/env python                                                                                                                                         
import time
start_time = time.time()




import sys
import os
maindir=os.getenv("GIT_HistoPlotterSys")
import argparse
from PlotterDataMC import PlotterDataMC
from OpenDictFile import OpenDictFile
from ExportShellCondorSetup_tamsa import Export


def Run(blind,Year,AnalyzerName,cut,x,procpath,dirname,outname,suffix,this_var,this_proc,normsyspaths):
    print "suffix",suffix
    myplotter=PlotterDataMC(Year,AnalyzerName,cut,x,procpath,dirname,outname,suffix,this_var,this_proc,normsyspaths)
    myplotter.SetBlind(blind)
    myplotter.RunDraw()
    del myplotter


def RunWithCondor(blind,Year,AnalyzerName,cut,x,procpath,dirname,outname,suffix,this_var,this_proc,normsyspaths):
    GIT_HistoPlotterSys=os.getenv("GIT_HistoPlotterSys")
    #export PYTHONPATH
    PYTHONPATH=os.getenv("PYTHONPATH")
    curdir=str(os.getcwd())

    
    ##batch setup##
    WORKDIR="/".join(['WORKDIR',AnalyzerName,str(Year),suffix,"isBlind__"+str(blind),cut,x])
    os.system('mkdir -p '+WORKDIR)
    jobname="plotter__"+AnalyzerName+"__"+Year
    submit=True
    ###############

    ##---condor command---##
    commandlist=[]
    #commandlist.append("export PYTHONPATH=${PYTHONPATH}:"+PYTHONPATH)
    commandlist.append("cd "+curdir)


    ##--Make python script
    pycommandlist=[]
    pycommandlist.append('import sys')
    pycommandlist.append('sys.path.append("'+GIT_HistoPlotterSys+'/script")')
    pycommandlist.append("from RunPlotterDataMC import Run")
    myarglist=[]
    myarglist_raw=[blind,Year,AnalyzerName,cut,x,procpath,dirname,outname,suffix,this_var,this_proc,normsyspaths]
    is_string = lambda value: isinstance(value, (str, unicode))

    for this_arg in myarglist_raw:
        if is_string(this_arg):
            True
            myarglist.append('"'+str(this_arg)+'"')
        else:
            myarglist.append(str(this_arg))
    myarg=",".join(myarglist)
    pycommandlist.append("Run("+myarg+")")
    pycommand="\n".join(pycommandlist)

    f=open(WORKDIR+"/Condor_RunPlotterDataMC.py","w")
    f.write(pycommand)
    f.close()
    ##--[END] Make python script

    commandlist.append("python "+WORKDIR+"/Condor_RunPlotterDataMC.py")
    command="&&".join(commandlist)

    
    #def Export(WORKDIR,command,jobname,submit,ncpu,memory=False,nretry=3,nmax):
    Export(WORKDIR,command,jobname,submit,1,False,3,1000)
    
    


    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plotter configuration')
    parser.add_argument('-a', dest='AnalyzerName', default="")
    parser.add_argument('-y', dest='year', default="")
    parser.add_argument('-d', dest='directory', default="")
    parser.add_argument('-s', dest='suffix', default="")
    parser.add_argument('-p', dest='procpath', default="")    
    parser.add_argument('-b', dest='blind', action="store_true",default=False)
    parser.add_argument('-n', dest='normsyspaths', default=False)
    parser.add_argument('--print', dest='print_cut_and_x', action="store_true",default=False)


    parser.add_argument('-c', dest='this_cut', default="")
    parser.add_argument('-v', dest='this_var', default="")
    parser.add_argument('-x', dest='this_x', default="")
    parser.add_argument('--proconly', dest='this_proc', default="")
    parser.add_argument('--condor', dest='condor', action="store_true", default=False)


    args = parser.parse_args()
    AnalyzerName=args.AnalyzerName
    year=args.year
    directory=args.directory
    suffix=args.suffix
    procpath=args.procpath
    blind=args.blind



    this_cut=args.this_cut

    if args.this_var!="" and args.this_var!="-":
        this_var=args.this_var.split(",")
    else:
        this_var=[]
    this_x=args.this_x

    if args.this_proc!="" and args.this_proc!="-":
        this_proc=args.this_proc.split(",")
    else:
        this_proc=[]
    normsyspaths=[]
    if args.normsyspaths:
        normsyspaths=args.normsyspaths.split(',')
    
    print_cut_and_x=args.print_cut_and_x

    cut_and_x_path=maindir+"/config/"+AnalyzerName+"/"+year+"/"+suffix+"/cut_and_x.py"
    cut_and_x=OpenDictFile(cut_and_x_path)
    if(print_cut_and_x):
        print cut_and_x
        exit()

    
    ncut=len(cut_and_x)
    icut=0

    ##
    print this_cut,this_var,this_x,this_proc


    for cut in cut_and_x:
        print icut+1,'/',ncut
        for x in cut_and_x[cut]:
            if this_cut!="" and this_cut!="-":
                if cut!=this_cut : continue
            if this_x!="" and this_x!="-": 
                if x!=this_x : continue
            print "-----------"
            print cut,x
            thisdir=directory+"/"+cut
            name=x
            if args.condor:
                RunWithCondor(blind,year,AnalyzerName,cut,x,procpath,thisdir,name,suffix,this_var,this_proc,normsyspaths)
                
            else:
                Run(blind,year,AnalyzerName,cut,x,procpath,thisdir,name,suffix,this_var,this_proc,normsyspaths)


        icut+=1


end_time = time.time()
execution_time = end_time - start_time
print("Script execution time: {:.6f} seconds".format(execution_time))
