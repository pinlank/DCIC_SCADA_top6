col_1 = ['var001', 'var002', 'var003', 'var004', 'var005', 'var006',
       'var007', 'var008', 'var009', 'var010', 'var011', 'var012', 'var013',
       'var014', 'var015', 'var016', 'var017', 'var018', 'var019', 'var020',
       'var021', 'var022', 'var023', 'var024', 'var025', 'var026', 'var027',
       'var028', 'var029', 'var030', 'var031', 'var032', 'var033', 'var034',
       'var035', 'var036', 'var037', 'var038', 'var039', 'var040', 'var041',
       'var042', 'var043', 'var044', 'var045', 'var046', 'var047', 'var048',
       'var049', 'var050', 'var051', 'var052', 'var053', 'var054', 'var055',
       'var056', 'var057', 'var058', 'var059', 'var060', 'var061', 'var062',
       'var063', 'var064', 'var065', 'var066', 'var067', 'var068']
col_8 = ['var001', 'var004', 'var005', 'var038', 'var042', 'var046', 'var050',
       'var060']

col_26 = ['var002', 'var003', 'var006', 'var007', 'var011', 'var012', 'var014',
       'var018', 'var021', 'var022', 'var024', 'var028', 'var029', 'var030',
       'var033', 'var035', 'var036', 'var037', 'var040', 'var045', 'var051',
       'var052', 'var055', 'var057', 'var062', 'var067']

col_19 = ['var013', 'var015', 'var016', 'var020', 'var027', 'var031', 'var032',
       'var034', 'var041', 'var043', 'var047', 'var049', 'var053', 'var054',
       'var056', 'var058', 'var061', 'var066', 'var068']

col_15 = ['var008', 'var009', 'var010', 'var017', 'var019', 'var023', 'var025',
       'var026', 'var039', 'var044', 'var048', 'var059', 'var063', 'var064',
       'var065']




def precise(y,y_pred):
    labels = y_pred.get_label()
    f = np.nanmean(np.exp(-100*np.abs(y-labels)/np.maximum(np.abs(y),10**(-15))))
#     f = np.nansum(np.exp(-100*np.abs(y-labels)/np.maximum(np.abs(y),10**(-15))))/23030489
    return 'lgb_feval', f, True

def precise1(y,y_pred,k):
    f = np.exp(-k*np.abs(y-y_pred)/np.maximum(np.abs(y),10**(-15)))
    return f

def time_extact(x,i):
    if i =='year':
        out  = x.dt.year
    elif i =='month':
        out  = x.dt.month
    elif i =='minute':
        out  = x.dt.minute
    elif i =='day':
        out  = x.dt.day
    elif i =='second':
        out  = x.dt.second
    elif i =='hour':
        out  = x.dt.hour
    elif i =='week':
        out  = x.dt.weekday
    return out