from client import DeadCodeUnreachableAstPrunerClient

def main():
    client = DeadCodeUnreachableAstPrunerClient()
    res = client.identify_dead_code_branches()
    print('Dead Code AST Pruner: ' + res['prune_audit_id'] + ' (' + res['repository_path'] + ')')
    print('Dead Functions: ' + str(res['unreachable_functions_count']) + ' | Obsolete Flags: ' + str(res['obsolete_feature_flags_detected']))
    print('Manifest URL: ' + res['dead_code_manifest_url'])

if __name__ == '__main__':
    main()
